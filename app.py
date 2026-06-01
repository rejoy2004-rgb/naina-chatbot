import streamlit as st
import os

from dotenv import load_dotenv
from openai import OpenAI

from rag.retrieve import retrieve_context

# =====================================
# OPENROUTER SETUP
# =====================================

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    st.error("OPENROUTER_API_KEY not found.")
    st.stop()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Naina AI",
    page_icon="👁️",
    layout="centered"
)

# =====================================
# HEADER
# =====================================

st.title("👁️ Naina AI")

st.subheader(
    "Eye Wellness & Vision Therapy Assistant"
)

st.caption(
    "Ask questions related to eye health, vision care, visual therapy, and eye wellness."
)

# =====================================
# USER INPUT
# =====================================

question = st.text_input(
    "Ask your eye-health question"
)

# =====================================
# ASK BUTTON
# =====================================

if st.button("Ask"):

    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    try:

        # ===============================
        # RETRIEVE CONTEXT
        # ===============================

        with st.spinner("Searching knowledge base..."):

            context = retrieve_context(question)

        # ===============================
        # CHECK CONTEXT
        # ===============================

        if not context.strip():

            st.warning(
                "I couldn't find relevant information in the knowledge base."
            )
            st.stop()

        # ===============================
        # OPENROUTER RESPONSE
        # ===============================

        with st.spinner("Generating response..."):

            response = client.chat.completions.create(
                model="deepseek/deepseek-chat-v3",
                messages=[
                    {
                        "role": "system",
                        "content": """
You are Naina AI, an Eye Wellness and Vision Therapy Assistant.

Your purpose:
- Help users understand eye health conditions.
- Use ONLY the provided knowledge base context.
- Explain information in simple and patient-friendly language.
- Be professional, supportive, and educational.

IMPORTANT RULES:

1. Answer ONLY eye-health and vision-related questions.

2. Use the provided context as the primary source.

3. If the answer is not present in the context, say:
"I couldn't find specific information in the Naina AI knowledge base."

4. Never diagnose diseases.

5. Never prescribe medications.

6. Never provide emergency medical advice.

7. Encourage professional consultation when needed.

8. Keep explanations easy to understand.

Response Format:

## 👁️ Eye Health Summary

Provide a short explanation.

## 📋 Possible Causes

Provide bullet points only if supported by context.

## ✅ Recommended Care

Provide safe eye-care recommendations.

## ⚠️ When to Seek Professional Help

Mention warning signs or persistent symptoms.

## 📌 Disclaimer

This information is educational and is not a medical diagnosis or treatment recommendation.
"""
                    },
                    {
                        "role": "assistant",
                        "content": f"""
Knowledge Base Context:

{context}
"""
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            )

            answer = (
                response
                .choices[0]
                .message
                .content
            )

        # ===============================
        # DISPLAY RESPONSE
        # ===============================

        st.success(
            "👁️ Naina AI Knowledge-Based Response"
        )

        st.markdown(answer)

    except Exception as e:

        st.error(
            f"Error: {e}"
        )

# =====================================
# FOOTER
# =====================================

st.divider()

with st.expander("About Naina AI"):

    st.markdown("""
### 👁️ Naina AI

Naina AI is an Eye Wellness & Vision Therapy Assistant designed to provide educational information about:

- Eye wellness
- Visual therapy
- Dry eye conditions
- Amblyopia
- Myopia
- Hyperopia
- Binocular vision
- Eye strain
- Vision care

### Technology Used

- OpenRouter
- DeepSeek Chat V3
- Retrieval Augmented Generation (RAG)
- ChromaDB Vector Store
- Ophthalmology Knowledge Base

### Important Disclaimer

Naina AI provides educational information only and is not a substitute for professional medical advice, diagnosis, or treatment.
""")