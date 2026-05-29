from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import google.generativeai as genai
from rag.retrieve import retrieve_context

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

app = FastAPI()


class ChatRequest(BaseModel):
    question: str


@app.post("/chat")
def chat(request: ChatRequest):

    context = retrieve_context(
        request.question
    )

    prompt = f"""
    Context:
    {context}

    Question:
    {request.question}

    Answer:
    """

    response = model.generate_content(
        prompt
    )

    return {
        "answer": response.text
    }