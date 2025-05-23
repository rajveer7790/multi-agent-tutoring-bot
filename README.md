# Multi-Agent Tutoring Bot

An intelligent tutoring system that uses multiple specialized AI agents to provide subject-specific assistance. Built using FastAPI and Google's Gemini API.

**Link to the chatbot - [Click here](https://www.multi-agent-tutoring-bot-production.up.railway.app)

## Architecture

The system consists of three main components:

1. **Tutor Agent**: The main interface that receives user queries and delegates them to specialized agents
2. **Specialist Agents**:
   - Math Agent: Handles mathematical queries and calculations
   - Physics Agent: Handles physics-related questions and constant lookups
3. **Tools**:
   - Calculator tool for mathematical operations
   - Physics constants lookup tool

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/yourusername/multi-agent-tutoring-bot.git
cd multi-agent-tutoring-bot
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

5. Run the application:

```bash
uvicorn app.main:app --reload
```

The application will be available at `http://localhost:8000`

## Project Structure

```
multi-agent-tutoring-bot/
├── app/
│   ├── agents/
│   │   ├── tutor_agent.py
│   │   ├── math_agent.py
│   │   └── physics_agent.py
│   ├── tools/
│   │   ├── calculator.py
│   │   └── physics_constants.py
│   ├── main.py
│   └── templates/
│       └── index.html
├── requirements.txt
├── .env
└── README.md
```

## API Endpoints

- `POST /api/query`: Submit a question to the tutoring system
- `GET /`: Web interface for interacting with the tutoring system

## Deployment

The application is deployed on [Vercel/Railway] and can be accessed at [your-deployment-url]

## Development Notes

- The system uses Google's Gemini API for natural language processing
- FastAPI provides the backend API and serves the web interface
- The frontend is built with HTML, CSS, and JavaScript for a simple but effective user experience
