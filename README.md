AI-First CRM – HCP Interaction Module
📌 Overview

This project is an AI-powered CRM system designed for Healthcare Professional (HCP) interaction tracking. It provides both a structured form and conversational AI interface to log and manage interactions.


🚀 Tech Stack
Frontend: React + Redux
Backend: FastAPI (Python)
AI Agent: LangGraph
LLM: Groq (gemma2-9b-it)
Database: SQLite (can be replaced with MySQL/PostgreSQL)


🤖 Key Features
Chat-based interaction logging

Structured data extraction using LLM

Edit existing interactions

AI-based next action suggestions

Compliance checking for pharma rules

Interaction history tracking

🛠️ LangGraph Agent Role
The LangGraph agent acts as an intelligent assistant for field representatives by:

Understanding natural language input

Extracting structured interaction data

Routing tasks to appropriate tools

Automating CRM workflows



🧩 Tools Implemented
Log Interaction Tool

Converts natural language into structured CRM data

Stores interaction in database

Edit Interaction Tool

Updates existing interaction fields

Fetch Insights Tool

Retrieves past interaction history

Suggest Next Action Tool

Recommends follow-ups using AI

Compliance Check Tool

Flags non-compliant pharmaceutical content


⚙️ Setup Instructions
Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
Frontend
cd frontend
npm install
npm start


🌐 API Endpoints
POST /chat → AI interaction
GET /interactions → Fetch all interactions
🧪 Sample Request
{
  "message": "Met Dr Sharma, discussed insulin dosage"
}
