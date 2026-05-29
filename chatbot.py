import os
from dotenv import load_dotenv
import google.generativeai as genai
from database import create_database
from database import save_message
from database import load_messages
from auth import signup
from auth import login

from rag.retrieve import retrieve_context

# DATABASE SETUP
create_database()

# GEMINI SETUP
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY not found in .env file")
    exit()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# NAINA SYSTEM PROMPT
SYSTEM_PROMPT = """
You are Naina, an intelligent eye wellness and visual therapy assistant.

You help users understand:

- eye strain
- dry eyes
- visual therapy
- amblyopia
- binocular vision
- convergence insufficiency
- eye exercises
- screen fatigue
- eye coordination
- visual wellness

Rules:

1. Use the provided context whenever possible.
2. Explain concepts in simple language.
3. Never diagnose diseases.
4. Never prescribe medicines.
5. Encourage consultation with qualified eye care professionals for medical concerns.
6. If information is not available in the context, clearly mention it.
"""

# WELCOME SCREEN
print("      Welcome to Naina AI ")

# AUTHENTICATION
while True:

    print("\n1. Sign Up")
    print("2. Login")

    choice = input("\nChoose option: ")

    if choice == "1":

        signup()

    elif choice == "2":

        user_id = login()

        if user_id:
            break

    else:

        print("Invalid choice. Try again.")

# LOAD CHAT HISTORY
messages = load_messages(user_id)

print("\nNaina AI Chatbot")
print("Type 'exit' to quit.\n")

# CHAT LOOP
while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":

        print("\nNaina: Goodbye! Take care of your eyes ")
        break

    # Save User Message
    save_message(
        user_id,
        "user",
        user_input
    )

    messages.append({
        "role": "user",
        "content": user_input
    })

    # Retrieve Context From Vector Database
    try:

        context = retrieve_context(user_input)

    except Exception as e:

        context = ""
        print(f"RAG Error: {e}")

    # Build Conversation History
    conversation_history = ""

    for msg in messages[-10:]:

        conversation_history += (
            f"{msg['role']}: {msg['content']}\n"
        )

    # Build Prompt

    prompt = f"""
{SYSTEM_PROMPT}

Retrieved Context:
{context}

Conversation History:
{conversation_history}

User Question:
{user_input}

Instructions:
- Use the retrieved context when possible.
- If context is missing, answer based on your eye wellness knowledge.
- Keep explanations simple.
- Mention eye exercises when relevant.
- Never diagnose diseases.

Answer:
"""

    # Gemini Response
    try:

        response = model.generate_content(prompt)

        ai_reply = response.text

    except Exception as e:

        ai_reply = f"Error generating response: {e}"

    # Save AI Reply
    save_message(
        user_id,
        "assistant",
        ai_reply
    )

    messages.append({
        "role": "assistant",
        "content": ai_reply
    })

    # Print AI Reply
    print("\nNaina:")
    print(ai_reply)
    print()