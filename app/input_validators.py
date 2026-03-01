# app/input_validators.py

from app.exceptions import ValidationError
from app.calculator_config import Config


def validate_number(value: str) -> float:
    """
    Validate and convert input to float.
    Ensures numeric input and max value constraints.
    """
    try:
        number = float(value)
    except ValueError:
        raise ValidationError("Input must be a numeric value.")

    if abs(number) > Config.MAX_INPUT_VALUE:
        raise ValidationError("Input exceeds maximum allowed value.")

    return round(number, Config.PRECISION)