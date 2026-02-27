# app/calculation.py

from datetime import datetime


class Calculation:
    """
    Represents a single calculation performed by the calculator.
    Stores operation name, operands, result, and timestamp.
    """

    def __init__(self, operation: str, a: float, b: float, result: float):
        self.operation = operation
        self.a = a
        self.b = b
        self.result = result
        self.timestamp = datetime.now()

    def to_dict(self) -> dict:
        """Convert calculation to dictionary (for CSV saving later)."""
        return {
            "operation": self.operation,
            "a": self.a,
            "b": self.b,
            "result": self.result,
            "timestamp": self.timestamp.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict):
        """Recreate Calculation from dictionary."""
        obj = cls(
            operation=data["operation"],
            a=float(data["a"]),
            b=float(data["b"]),
            result=float(data["result"]),
        )
        obj.timestamp = datetime.fromisoformat(data["timestamp"])
        return obj