import pytest
from app.operations import (
    Operation,
    Add, Subtract, Multiply, Divide,
    Power, Root, Modulus,
    IntegerDivide, Percentage,
    AbsoluteDifference, OperationFactory
)
from app.exceptions import OperationError


def test_add():
    assert Add().execute(2, 3) == 5


def test_subtract():
    assert Subtract().execute(5, 3) == 2


def test_multiply():
    assert Multiply().execute(4, 3) == 12


def test_divide():
    assert Divide().execute(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(OperationError):
        Divide().execute(10, 0)


def test_power():
    assert Power().execute(2, 3) == 8


def test_root():
    assert Root().execute(27, 3) == 3


def test_root_zero_degree():
    with pytest.raises(OperationError):
        Root().execute(16, 0)


def test_root_even_degree_negative_number():
    with pytest.raises(OperationError):
        Root().execute(-16, 2)


def test_modulus():
    assert Modulus().execute(10, 3) == 1


def test_modulus_by_zero():
    with pytest.raises(OperationError):
        Modulus().execute(10, 0)


def test_integer_divide():
    assert IntegerDivide().execute(10, 3) == 3


def test_integer_divide_by_zero():
    with pytest.raises(OperationError):
        IntegerDivide().execute(10, 0)


def test_percentage():
    assert Percentage().execute(50, 200) == 25


def test_percentage_zero_denominator():
    with pytest.raises(OperationError):
        Percentage().execute(50, 0)


def test_absolute_difference():
    assert AbsoluteDifference().execute(10, 3) == 7


def test_factory_valid():
    op = OperationFactory.create_operation("add")
    assert op.execute(2, 2) == 4


def test_factory_invalid():
    with pytest.raises(OperationError):
        OperationFactory.create_operation("unknown")


def test_get_available_operations():
    ops = OperationFactory.get_available_operations()
    assert "add" in ops
    assert "power" in ops


def test_operation_abstract_method_body():
    assert Operation.execute(object(), 1, 2) is None
