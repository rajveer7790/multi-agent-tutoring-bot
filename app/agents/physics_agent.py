import google.generativeai as genai
from typing import Dict, Any
from ..tools.physics_constants import PhysicsConstants

class PhysicsAgent:
    """A specialized agent for handling physics-related queries."""
    
    def __init__(self, api_key: str):
        """Initialize the Physics Agent with Gemini API configuration."""
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        self.constants = PhysicsConstants()
    
    async def process_query(self, query: str) -> Dict[str, Any]:
        """
        Process a physics query using the Gemini API and physics constants tool.
        
        Args:
            query: The user's physics question
            
        Returns:
            A dictionary containing the response and any constants used
        """
        # First, use Gemini to analyze if the query requires physical constants
        prompt = f"""
        Analyze this physics query and determine if it requires physical constants:
        {query}
        
        If it requires constants, list the constants needed (e.g., 'speed_of_light', 'gravitational_constant').
        If it's a conceptual question, respond with 'conceptual'.
        """
        
        response = self.model.generate_content(prompt)
        analysis = response.text.strip()
        
        if analysis.lower() == 'conceptual':
            # For conceptual questions, use Gemini to provide a concise explanation
            explanation_prompt = f"""
            Provide a brief, clear explanation for this physics concept in 2-3 sentences:
            {query}
            """
            explanation = self.model.generate_content(explanation_prompt)
            return {
                "type": "conceptual",
                "response": explanation.text,
                "constants": None
            }
        else:
            # For questions requiring constants, look them up and provide context
            constants_used = {}
            for constant_name in analysis.split(','):
                constant_name = constant_name.strip()
                constant_data = self.constants.lookup(constant_name)
                if constant_data:
                    constants_used[constant_name] = constant_data
            
            if not constants_used:
                return {
                    "type": "error",
                    "response": "Could not identify relevant physical constants for this query.",
                    "constants": None
                }
            
            # Use Gemini to provide a concise explanation incorporating the constants
            explanation_prompt = f"""
            Using these physical constants: {constants_used}
            Provide a brief, clear explanation for this physics question in 2-3 sentences:
            {query}
            """
            explanation = self.model.generate_content(explanation_prompt)
            
            return {
                "type": "constants",
                "response": explanation.text,
                "constants": constants_used
            } 