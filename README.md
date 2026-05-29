# 👁️ Naina AI — Eye Wellness & Visual Therapy Assistant

Naina AI is a domain-specific chatbot designed to assist users with eye wellness, visual therapy, amblyopia, binocular vision disorders, dry eyes, screen fatigue, eye exercises, and related visual health topics.

The chatbot uses:

* Gemini 2.5 Flash (LLM)
* Semantic RAG (Retrieval-Augmented Generation)
* ChromaDB Vector Database
* Sentence Transformers Embeddings
* SQLite Database
* User Authentication System
* PDF Knowledge Base

---

# Features

## User Authentication

* User Signup
* User Login
* Secure account management
* SQLite-based storage

## Chat Memory

* Stores user conversations
* Retrieves previous messages
* Maintains conversation context

## Gemini AI Integration

* Powered by Gemini 2.5 Flash
* Natural language understanding
* Domain-focused responses

## Semantic RAG

* Reads PDF documents
* Splits documents into chunks
* Generates embeddings
* Stores embeddings in ChromaDB
* Retrieves relevant information before generating answers

## Eye Wellness Knowledge

Naina can assist with:

* Amblyopia
* Myopia
* Hyperopia
* Dry Eye Syndrome
* Eye Strain
* Visual Fatigue
* Convergence Insufficiency
* Binocular Vision Disorders
* Visual Therapy
* Eye Exercises
* Screen Fatigue
* Visual Comfort

---

# Project Structure

```text
naina_chatbot/
│
├── chatbot.py
├── auth.py
├── database.py
├── naina.db
│
├── documents/
│   ├── paper1.pdf
│   ├── paper2.pdf
│   └── paper3.pdf
│
├── rag/
│   ├── create_vector_db.py
│   └── retrieve.py
│
├── vector_db/
│
├── .env
├── requirements.txt
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/rejoy2004-rgb/naina-chatbot.git
cd naina-chatbot
```

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Gemini API Setup

Create a `.env` file in the root directory.

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

Get a Gemini API key from:

https://aistudio.google.com/app/apikey

---

# Add PDF Documents

Place all research papers inside:

```text
documents/
```

Example:

```text
documents/
├── Amblyopia.pdf
├── DryEyeSyndrome.pdf
├── VisualTherapy.pdf
```

---

# Build Vector Database

Generate embeddings and create the vector database:

```bash
python rag/create_vector_db.py
```

Expected Output:

```text
Loaded 120 pages
Created 450 chunks

Vector DB Created Successfully
```

---

# Run Chatbot

```bash
python chatbot.py
```

---

# Example Usage

```text
Welcome to Naina AI

1. Sign Up
2. Login
```

After login:

```text
You: What does the amblyopia paper say?

Naina:
Amblyopia is a visual development disorder...
```

---

# Semantic RAG Pipeline

```text
User Question
       ↓
Vector Search
       ↓
ChromaDB
       ↓
Relevant PDF Chunks
       ↓
Gemini 2.5 Flash
       ↓
Final Response
```

---

# Technologies Used

* Python
* Gemini 2.5 Flash
* Google Generative AI SDK
* LangChain
* ChromaDB
* Sentence Transformers
* SQLite
* PyPDF
* Python Dotenv

---

# Future Improvements

* Source Citations
* PDF Page References
* Streamlit Web Interface
* Voice Assistant Support
* Multi-PDF Knowledge Base
* Clinical FAQ System
* Website Integration
* Doctor Recommendation System
* Analytics Dashboard
* Cloud Deployment

---

# Disclaimer

Naina AI is an educational and informational assistant.

It is not intended to diagnose, treat, cure, or prevent any disease. Users should always consult qualified eye-care professionals for medical advice and treatment.

---

# Author

Rejoy Besra

Naina AI — Eye Wellness & Visual Therapy Assistant
