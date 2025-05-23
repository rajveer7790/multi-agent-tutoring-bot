import os
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv
from .agents.tutor_agent import TutorAgent

# Load environment variables
load_dotenv()

# Get API key and validate
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set")

# Initialize FastAPI app
app = FastAPI(title="Multi-Agent Tutoring Bot")

# Initialize templates
templates = Jinja2Templates(directory="app/templates")

# Initialize tutor agent
tutor_agent = TutorAgent(api_key)

class Query(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the home page with the chat interface."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/query")
async def process_query(query: Query):
    """Process a query through the tutor agent."""
    try:
        if not query.text.strip():
            raise HTTPException(status_code=400, detail="Query cannot be empty")
            
        response = await tutor_agent.process_query(query.text)
        if not response:
            raise HTTPException(status_code=500, detail="No response from tutor agent")
            
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 