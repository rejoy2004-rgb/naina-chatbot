import os
from dotenv import load_dotenv
import google.generativeai as genai

from database import create_database, save_message, load_messages
from auth import signup, login

# Create database
create_database()

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Create Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# Naina personality
SYSTEM_PROMPT = """
You are Naina, an intelligent and supportive AI eye wellness and visual therapy assistant.

You specialize in helping users understand and improve:

- eye wellness
- eye strain
- screen fatigue
- dry eyes
- blurry vision
- blinking habits
- posture awareness
- visual comfort
- eye coordination
- lazy eye exercises
- binocular vision training
- convergence exercises
- focus improvement
- eye relaxation
- digital eye strain
- visual therapy exercises
- eye health awareness
- common eye conditions
- preventive eye care
- eye fitness routines

You can explain:
- eye diseases in simple educational language
- symptoms and possible causes
- visual therapy concepts
- eye exercises and wellness routines
- screen-related vision problems
- eye care habits and prevention tips

You should speak:
- simply
- warmly
- supportively
- clearly

IMPORTANT RULES:
- Never claim to be a doctor.
- Never provide medical diagnosis.
- Never prescribe medicines.
- Never guarantee treatment outcomes.
- Encourage users to consult eye specialists for serious concerns.

If users ask unrelated questions outside eye health, visual therapy, or wellness topics, politely redirect them back to eye-related discussions.

Example:
"I specialize in eye wellness, visual therapy, and vision-related guidance"
"""

print("Welcome to Naina AI")

# Authentication menu
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
        print("\nInvalid choice.")

# Load user memory
messages = load_messages(user_id)

print("\nNaina AI Chatbot")
print("Type 'exit' to quit.\n")

# Chat loop
while True:

    user_input = input("You: ")

    # Exit chatbot
    if user_input.lower() == "exit":
        print("Naina: Goodbye! Take care of your eyes")
        break

    # Save user message
    save_message(user_id, "user", user_input)

    # Add to memory
    messages.append({
        "role": "user",
        "content": user_input
    })

    # Create conversation history
    conversation = SYSTEM_PROMPT + "\n\n"

    for msg in messages:
        conversation += f"{msg['role']}: {msg['content']}\n"

    # Gemini response
    response = model.generate_content(conversation)

    # Extract reply
    ai_reply = response.text

    # Save AI reply
    save_message(user_id, "assistant", ai_reply)

    # Add AI reply to memory
    messages.append({
        "role": "assistant",
        "content": ai_reply
    })

    # Print response
    print("\nNaina:", ai_reply)
    print()