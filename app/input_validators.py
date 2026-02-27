from app.exceptions import ValidationError
from app.calculator_config import Config

def validate_number(value_str: str) -> float:
    """Validates that the input string is a number and within bounds."""
    try:
        value = float(value_str)
    except ValueError:
        raise ValidationError(f"Invalid input: '{value_str}' is not a valid number.")
    
    max_val = float(Config.MAX_INPUT_VALUE)
    if abs(value) > max_val:
        raise ValidationError(f"Input {value} exceeds the maximum allowed value of {max_val}.")
    
    return value