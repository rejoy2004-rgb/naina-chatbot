import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
from rag.retrieve import retrieve_context


# CONFIG
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    st.error("OPENROUTER_API_KEY not found")
    st.stop()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

st.set_page_config(
    page_title="Naina AI",
    page_icon="👁️",
    layout="centered"
)



# UI
st.title("👁️ Naina AI")

st.caption(
    "Eye Wellness & Vision Therapy Assistant"
)

model = st.sidebar.selectbox(
    "Select Model",
    [
        "deepseek/deepseek-chat-v3",
        "google/gemini-2.5-flash"
    ]
)


# SESSION STATE
if "messages" not in st.session_state:
    st.session_state.messages = []

if "assessment_active" not in st.session_state:
    st.session_state.assessment_active = False

if "assessment_questions" not in st.session_state:
    st.session_state.assessment_questions = 0


# CHAT HISTORY
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


# EMERGENCY DETECTION

EMERGENCY_KEYWORDS = [
    "sudden vision loss",
    "blindness",
    "eye injury",
    "chemical splash",
    "severe eye pain",
    "retinal detachment",
    "flashes of light"
]


def emergency_detected(text):

    text = text.lower()

    return any(
        keyword in text
        for keyword in EMERGENCY_KEYWORDS
    )


# SYMPTOM DETECTION
SYMPTOM_KEYWORDS = [
    "dry eye",
    "dry eyes",
    "itching",
    "burning",
    "red eye",
    "red eyes",
    "blurry",
    "blurred",
    "vision",
    "eye strain",
    "myopia",
    "hyperopia",
    "glaucoma",
    "cataract",
    "astigmatism",
    "pain"
]


def symptom_query(text):

    text = text.lower()

    return any(
        word in text
        for word in SYMPTOM_KEYWORDS
    )


# SYSTEM PROMPT
SYSTEM_PROMPT = """
You are Naina AI.

You are an ophthalmology assistant.

RULES:

1. If a user reports symptoms:
   Ask ONE follow-up question at a time.

2. Gather:
   - duration
   - severity
   - associated symptoms
   - screen exposure
   - risk factors

3. Continue asking questions until
   enough information exists.

4. Once enough information exists:

Provide:

## 👁️ Eye Health Summary

## 📋 Possible Causes

## ✅ Recommended Care

## ⚠️ When To Seek Professional Help

## 📌 Disclaimer

5. Never diagnose.

6. Never prescribe medicines.

7. Use provided knowledge base context.

8. Remember conversation history.

9. If enough information exists,
   stop asking questions and
   generate assessment.
"""

# USER INPUT
prompt = st.chat_input(
    "Ask Naina AI..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    try:

        # EMERGENCY
        if emergency_detected(prompt):

            reply = """
⚠️ **Possible Eye Emergency**

Your symptoms may require urgent medical attention.

Please seek immediate care from an ophthalmologist or emergency department.

This assistant cannot assess emergency conditions.
"""

        else:

            # START ASSESSMENT

            if (
                symptom_query(prompt)
                and not st.session_state.assessment_active
            ):

                st.session_state.assessment_active = True
                st.session_state.assessment_questions = 0

            # BUILD CONTEXT
            recent_user_messages = " ".join(
                [
                    msg["content"]
                    for msg in st.session_state.messages[-10:]
                    if msg["role"] == "user"
                ]
            )

            context = retrieve_context(
                recent_user_messages
            )

            messages = [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                }
            ]

            messages.append(
                {
                    "role": "system",
                    "content": f"""
Knowledge Base Context:

{context}
"""
                }
            )

            messages.extend(
                st.session_state.messages
            )

            with st.spinner(
                "Analyzing..."
            ):

                response = (
                    client.chat.completions.create(
                        model=model,
                        messages=messages,
                        temperature=0.3
                    )
                )

            reply = (
                response
                .choices[0]
                .message
                .content
            )

            # TRACK QUESTIONS
            if "?" in reply:

                st.session_state.assessment_questions += 1

            if (
                "## 👁️ Eye Health Summary"
                in reply
            ):

                st.session_state.assessment_active = False
                st.session_state.assessment_questions = 0


        # DISPLAY RESPONSE
        with st.chat_message(
            "assistant"
        ):
            st.markdown(reply)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )


# SIDEBAR
with st.sidebar:

    st.markdown("### About Naina AI")

    st.markdown(
        """
- DeepSeek V3
- Gemini Flash
- RAG Knowledge Base
- ChromaDB
- Conversational Memory
- Dynamic Eye Assessment
- Emergency Detection
"""
    )

    if st.button(
        "Clear Chat"
    ):
        st.session_state.messages = []
        st.session_state.assessment_active = False
        st.session_state.assessment_questions = 0
        st.rerun()