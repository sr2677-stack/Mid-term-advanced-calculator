import pytest
from app.input_validators import validate_number
from app.exceptions import ValidationError
from app.calculator_config import Config


def test_valid_number():
    result = validate_number("10")
    assert isinstance(result, float)


def test_invalid_number():
    with pytest.raises(ValidationError):
        validate_number("abc")


def test_exceed_max_value():
    too_large = str(Config.MAX_INPUT_VALUE + 1)

    with pytest.raises(ValidationError):
        validate_number(too_large)