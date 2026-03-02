from abc import ABC, abstractmethod
from app.exceptions import OperationError


class Operation(ABC):
    """
    Abstract base class for all calculator operations.
    Each concrete operation must implement execute().
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
        if a < 0 and b % 2 == 0:
            raise OperationError("Even root of negative number is not allowed.")
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
    Factory responsible for creating operation instances.
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
        operation_name = operation_name.lower()

        if operation_name not in cls._operations:
            raise OperationError(f"Invalid operation: {operation_name}")

        return cls._operations[operation_name]()

    @classmethod
    def get_available_operations(cls):
        """
        Returns a list of available operation names.
        Used by dynamic help menu.
        """
        return list(cls._operations.keys())