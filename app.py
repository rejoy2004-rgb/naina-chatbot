import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
from rag.retrieve import retrieve_context

# Gemini Setup
load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-1.5-flash"
)

# Streamlit UI
st.set_page_config(
    page_title="Naina AI"
)

st.title(" Naina AI")
st.subheader(
    "Eye Wellness & Visual Therapy Assistant"
)

question = st.text_input(
    "Ask a question"
)

# Ask Button
if st.button("Ask"):

    if question.strip() == "":

        st.warning(
            "Please enter a question."
        )

    else:

        with st.spinner(
            "Searching knowledge base..."
        ):

            context = retrieve_context(
                question
            )

        # No relevant context found
        if not context or len(context.strip()) < 20:

            st.markdown("## Answer")

            st.warning(
                "I could not find this information in my knowledge base."
            )

        else:

            prompt = f"""
You are Naina AI.

You are an Eye Wellness and Visual Therapy Assistant.

Answer ONLY using the information provided in the context.

Do not make up information.

If the answer is not available in the context, say:

"I could not find this information in my knowledge base."

Context:
{context}

Question:
{question}

Answer:
"""
            try:
                with st.spinner(
                    "Generating answer..."
                ):
                    response = model.generate_content(
                        prompt
                    )
                st.markdown(
                    "## Answer"
                )
                st.write(
                    response.text
                )
            except Exception as e:
                error_text = str(e)

                # Gemini quota exceeded
                if (
                    "ResourceExhausted" in error_text
                    or "429" in error_text
                    or "quota" in error_text.lower()
                ):

                    st.warning(
                        "Gemini quota reached. Showing retrieved information from knowledge base."
                    )

                    st.markdown(
                        "## Retrieved Information"
                    )

                    st.write(
                        context
                    )
                else:
                    st.error(
                        f"Error: {error_text}"
                    )