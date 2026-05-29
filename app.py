import streamlit as st
import os

from dotenv import load_dotenv
import google.generativeai as genai

from rag.retrieve import retrieve_context

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

st.set_page_config(
    page_title="Naina AI",
    page_icon="👁️"
)

st.title("👁️ Naina AI")
st.subheader("Eye Wellness & Visual Therapy Assistant")

question = st.text_input(
    "Ask a question"
)

if st.button("Ask"):

    with st.spinner("Thinking..."):

        context = retrieve_context(question)

        prompt = f"""
You are Naina AI.

Context:
{context}

Question:
{question}

Answer:
"""

        response = model.generate_content(
            prompt
        )

        st.write(response.text)