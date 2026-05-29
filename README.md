# 👁️ Naina AI — Eye Wellness & Visual Therapy Assistant

## Overview

Naina AI is an intelligent eye wellness and visual therapy assistant designed to help users improve visual comfort, reduce digital eye strain, and understand eye health through AI-powered conversations.

The assistant provides educational guidance related to:

* Eye wellness
* Screen fatigue
* Dry eyes
* Blinking habits
* Posture awareness
* Visual therapy exercises
* Eye coordination
* Focus improvement
* Digital eye strain
* Preventive eye care

Naina is designed as a supportive AI companion focused specifically on eye wellness and visual therapy.

---

# Features

## ✅ AI Eye Wellness Chatbot

* Conversational AI assistant powered by Gemini API
* Context-aware responses
* Friendly and supportive personality

## ✅ User Authentication

* User Sign Up
* User Login
* Multi-user support

## ✅ Persistent Chat Memory

* Stores conversations using SQLite database
* Loads previous chat history automatically

## ✅ Eye Wellness Guidance

Naina can discuss:

* Eye strain
* Dry eyes
* Visual fatigue
* Eye exercises
* Lazy eye therapy
* Screen habits
* Focus improvement
* Posture awareness
* Vision wellness

## ✅ Domain-Specific AI

The chatbot is restricted mainly to:

* Eye wellness
* Visual therapy
* Eye health education

---

# Tech Stack

| Technology               | Purpose               |
| ------------------------ | --------------------- |
| Python                   | Backend logic         |
| Gemini API               | AI responses          |
| SQLite                   | Database              |
| python-dotenv            | Environment variables |
| Google Generative AI SDK | Gemini integration    |

---

# Project Structure

```bash
naina_chatbot/
│
├── chatbot.py          # Main chatbot application
├── auth.py             # User authentication
├── database.py         # Database functions
├── naina.db            # SQLite database
├── .env                # API keys
├── requirements.txt    # Python dependencies
└── README.md
```

---

# Installation Guide

## Step 1 — Clone Project

```bash
git clone <your_repository_link>
cd naina_chatbot
```

---

## Step 2 — Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

## Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Gemini API Setup

## Step 1 — Get Gemini API Key

Go to:

https://aistudio.google.com/

* Login with Google account
* Click "Get API Key"
* Create API key
* Copy the key

---

## Step 2 — Create `.env` File

Create a file named:

```bash
.env
```

Add:

```env
GEMINI_API_KEY=your_actual_gemini_api_key
```

---

# Run the Project

```bash
python chatbot.py
```

---

# Example Chat

```text
You: My eyes hurt after coding for long hours

Naina:
Extended screen exposure can contribute to digital eye strain 👁️

You may benefit from:
- frequent blinking
- screen breaks
- proper lighting
- focus shifting exercises
```

---

# Database

The project uses SQLite database:

```bash
naina.db
```

Tables:

* users
* messages

---

# Safety Disclaimer

Naina AI is an educational eye wellness assistant.

It:

* does NOT diagnose diseases
* does NOT prescribe medicines
* does NOT replace professional medical advice

Users should consult qualified eye care professionals for medical concerns.

---

# Future Improvements

Planned future features:

* Eye image analysis
* Blink detection
* Real-time webcam tracking
* Voice AI
* Personalized wellness scores
* Visual therapy games
* Eye fatigue prediction
* Wellness dashboards
* Mobile app integration

---

# Learning Goals of This Project

This project helps learn:

* AI chatbot development
* Gemini API integration
* Authentication systems
* SQLite databases
* Conversation memory
* AI prompt engineering
* Healthcare AI fundamentals

---

# Author

Developed by:
Rejoy Besra

Project:
Naina AI — Eye Wellness & Visual Therapy Assistant 👁️
