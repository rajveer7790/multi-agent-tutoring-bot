from typing import Dict, Optional

class PhysicsConstants:
    """A tool for looking up physical constants."""
    
    CONSTANTS: Dict[str, Dict[str, float]] = {
        "speed_of_light": {
            "value": 299792458.0,
            "unit": "m/s",
            "description": "Speed of light in vacuum"
        },
        "gravitational_constant": {
            "value": 6.67430e-11,
            "unit": "m³/kg/s²",
            "description": "Newtonian constant of gravitation"
        },
        "planck_constant": {
            "value": 6.62607015e-34,
            "unit": "J⋅s",
            "description": "Planck constant"
        },
        "electron_mass": {
            "value": 9.1093837015e-31,
            "unit": "kg",
            "description": "Electron mass"
        },
        "proton_mass": {
            "value": 1.67262192369e-27,
            "unit": "kg",
            "description": "Proton mass"
        },
        "avogadro_number": {
            "value": 6.02214076e23,
            "unit": "mol⁻¹",
            "description": "Avogadro constant"
        },
        "boltzmann_constant": {
            "value": 1.380649e-23,
            "unit": "J/K",
            "description": "Boltzmann constant"
        }
    }
    
    @staticmethod
    def lookup(constant_name: str) -> Optional[Dict[str, str]]:
        """
        Look up a physical constant by name.
        
        Args:
            constant_name: The name of the constant to look up
            
        Returns:
            A dictionary containing the constant's value, unit, and description,
            or None if the constant is not found
        """
        constant_name = constant_name.lower().replace(" ", "_")
        if constant_name in PhysicsConstants.CONSTANTS:
            constant_data = PhysicsConstants.CONSTANTS[constant_name]
            return {
                "value": str(constant_data["value"]),
                "unit": constant_data["unit"],
                "description": constant_data["description"]
            }
        return None
    
    @staticmethod
    def list_constants() -> Dict[str, Dict[str, str]]:
        """
        Get a list of all available constants.
        
        Returns:
            A dictionary of all constants with their values, units, and descriptions
        """
        return {
            name: {
                "value": str(data["value"]),
                "unit": data["unit"],
                "description": data["description"]
            }
            for name, data in PhysicsConstants.CONSTANTS.items()
        } 