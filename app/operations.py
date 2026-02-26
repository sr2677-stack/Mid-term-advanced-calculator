# app/operations.py

from abc import ABC, abstractmethod
from app.exceptions import OperationError


class Operation(ABC):
    """
    Abstract base class for all calculator operations.
    Each operation must implement the execute method.
    """

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass


# =========================
# Basic Arithmetic Operations
# =========================

class Add(Operation):
    def execute(self, a: float, b: float) -> float:
        return a + b


class Subtract(Operation):
    def execute(self, a: float, b: float) -> float:
        return a - b


class Multiply(Operation):
    def execute(self, a: float, b: float) -> float:
        return a * b


class Divide(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Cannot divide by zero.")
        return a / b


# =========================
# Advanced Operations
# =========================

class Power(Operation):
    def execute(self, a: float, b: float) -> float:
        return a ** b


class Root(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Root degree cannot be zero.")
        return a ** (1 / b)


class Modulus(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Cannot modulus by zero.")
        return a % b


class IntegerDivide(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Cannot perform integer division by zero.")
        return a // b


class Percentage(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise OperationError("Cannot calculate percentage with zero denominator.")
        return (a / b) * 100


class AbsoluteDifference(Operation):
    def execute(self, a: float, b: float) -> float:
        return abs(a - b)


# =========================
# Factory Pattern
# =========================

class OperationFactory:
    """
    Factory class responsible for creating operation instances.
    Implements the Factory Design Pattern.
    """

    _operations = {
        "add": Add,
        "subtract": Subtract,
        "multiply": Multiply,
        "divide": Divide,
        "power": Power,
        "root": Root,
        "modulus": Modulus,
        "int_divide": IntegerDivide,
        "percent": Percentage,
        "abs_diff": AbsoluteDifference,
    }

    @classmethod
    def create_operation(cls, operation_name: str) -> Operation:
        """
        Create and return an operation instance.

        :param operation_name: Name of the operation
        :return: Operation instance
        :raises OperationError: If operation is invalid
        """
        operation_name = operation_name.lower()

        if operation_name not in cls._operations:
            raise OperationError(f"Invalid operation: {operation_name}")

        return cls._operations[operation_name]()