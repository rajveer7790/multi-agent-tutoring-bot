import google.generativeai as genai
import math
import re
from typing import Dict, Any

class MathAgent:
    """A specialized agent for handling mathematical queries."""
    
    def __init__(self, api_key: str):
        """Initialize the Math Agent with Gemini API configuration."""
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')
    
    async def process_query(self, query: str) -> Dict[str, Any]:
        """
        Process a mathematical query using the Gemini API.
        
        Args:
            query: The user's mathematical question
            
        Returns:
            A dictionary containing the response and any calculations performed
        """
        # First, use Gemini to analyze the query
        prompt = f"""
        Analyze this mathematical query and determine its type:
        {query}
        
        Respond with exactly one of these options:
        - 'equation' if it's an equation to solve (contains =)
        - 'calculation' if it's a simple calculation
        - 'formula' if it's a formula application (like area, volume, etc.)
        - 'conceptual' if it's a conceptual question
        """
        
        response = self.model.generate_content(prompt)
        query_type = response.text.strip().lower()
        
        if query_type == 'conceptual':
            # For conceptual questions, use Gemini to provide a concise explanation
            explanation_prompt = f"""
            Provide a brief, clear explanation for this mathematical concept in 2-3 sentences:
            {query}
            """
            explanation = self.model.generate_content(explanation_prompt)
            return {
                "type": "conceptual",
                "response": explanation.text,
                "calculations": None
            }
        elif query_type == 'equation':
            # For equations, use Gemini to solve and explain
            solve_prompt = f"""
            Solve this equation and provide the solution in a clear, concise way:
            {query}
            
            Format your response as:
            1. The solution (x = value)
            2. A brief explanation of the steps (1-2 sentences)
            """
            solution = self.model.generate_content(solve_prompt)
            return {
                "type": "equation",
                "response": solution.text,
                "calculations": None
            }
        elif query_type == 'formula':
            # For formula applications, let Gemini handle the calculation and explanation
            formula_prompt = f"""
            For this geometric calculation: {query}
            
            1. Identify the shape and required formula
            2. Extract the given measurements
            3. Calculate the result
            4. Provide a brief, clear response in this format:
               "The [shape] has an area of [result] square [units]."
            
            Keep the response concise and include the calculation steps in 1-2 sentences.
            """
            
            formula_response = self.model.generate_content(formula_prompt)
            return {
                "type": "formula",
                "response": formula_response.text,
                "calculations": {
                    "query": query,
                    "result": formula_response.text
                }
            }
        else:
            # For calculation questions, use Gemini to solve and explain
            calc_prompt = f"""
            Solve this calculation: {query}
            
            Provide a clear, concise response in this format:
            1. The result of the calculation
            2. A brief explanation of the steps (1-2 sentences)
            
            Example format:
            "The result is [answer].
            [Brief explanation of how you got the answer]"
            """
            
            calc_response = self.model.generate_content(calc_prompt)
            return {
                "type": "calculation",
                "response": calc_response.text,
                "calculations": {
                    "query": query,
                    "result": calc_response.text
                }
            } 