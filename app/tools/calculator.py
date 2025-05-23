from typing import Union, Dict
import operator

class Calculator:
    """A simple calculator tool for basic arithmetic operations."""
    
    OPERATIONS = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow,
    }
    
    @staticmethod
    def calculate(expression: str) -> Union[float, str]:
        """
        Evaluate a mathematical expression.
        
        Args:
            expression: A string containing a mathematical expression
            
        Returns:
            The result of the calculation or an error message
        """
        try:
            # Split the expression into numbers and operators
            parts = expression.split()
            if len(parts) != 3:
                return "Invalid expression format. Please use format: 'number operator number'"
            
            num1 = float(parts[0])
            operator_symbol = parts[1]
            num2 = float(parts[2])
            
            if operator_symbol not in Calculator.OPERATIONS:
                return f"Unsupported operator: {operator_symbol}"
            
            if operator_symbol == '/' and num2 == 0:
                return "Error: Division by zero"
            
            result = Calculator.OPERATIONS[operator_symbol](num1, num2)
            return result
            
        except ValueError:
            return "Error: Invalid number format"
        except Exception as e:
            return f"Error: {str(e)}" 