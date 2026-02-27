import pytest
from app.input_validators import validate_number
from app.exceptions import ValidationError
from app.calculator_config import Config

def test_valid_numbers():
    assert validate_number("5") == 5.0
    assert validate_number("-10.5") == -10.5

def test_invalid_string():
    with pytest.raises(ValidationError):
        validate_number("hello")

def test_number_out_of_bounds():
    # temporarily set max value for testing
    original_max = Config.MAX_INPUT_VALUE
    Config.MAX_INPUT_VALUE = 100
    
    with pytest.raises(ValidationError):
        validate_number("101")
        
    # restore config
    Config.MAX_INPUT_VALUE = original_max