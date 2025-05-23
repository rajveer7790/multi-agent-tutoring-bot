import google.generativeai as genai
from typing import Dict, Any, Optional
from .math_agent import MathAgent
from .physics_agent import PhysicsAgent

class TutorAgent:
    """The main tutor agent that coordinates between specialist agents."""
    
    def __init__(self, api_key: str):
        """Initialize the Tutor Agent with specialist agents."""
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        self.math_agent = MathAgent(api_key)
        self.physics_agent = PhysicsAgent(api_key)
    
    async def process_query(self, query: str) -> Dict[str, Any]:
        """
        Process a query by determining the appropriate specialist agent and delegating the task.
        
        Args:
            query: The user's question
            
        Returns:
            A dictionary containing the response and metadata about which agent handled it
        """
        # Use Gemini to determine the subject area
        prompt = f"""
        Analyze this query and determine if it's primarily about mathematics or physics:
        {query}
        
        Respond with exactly one of these options:
        - 'mathematics'
        - 'physics'
        - 'other'
        """
        
        response = self.model.generate_content(prompt)
        subject = response.text.strip().lower()
        
        # Delegate to the appropriate specialist agent
        if subject == 'mathematics':
            result = await self.math_agent.process_query(query)
            return {
                "agent": "math",
                "subject": "mathematics",
                **result
            }
        elif subject == 'physics':
            result = await self.physics_agent.process_query(query)
            return {
                "agent": "physics",
                "subject": "physics",
                **result
            }
        else:
            # For other subjects, provide a concise response
            explanation_prompt = f"""
            Provide a brief, clear answer to this question in 2-3 sentences:
            {query}
            """
            explanation = self.model.generate_content(explanation_prompt)
            return {
                "agent": "general",
                "subject": "other",
                "type": "general",
                "response": explanation.text
            } 