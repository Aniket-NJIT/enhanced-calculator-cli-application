class CalculatorException(Exception):
    """Base exception for the calculator."""
    pass

class OperationError(CalculatorException):
    """Raised when an arithmetic operation fails (e.g., division by zero)."""
    pass

class ValidationError(CalculatorException):
    """Raised when user input is invalid."""
    pass