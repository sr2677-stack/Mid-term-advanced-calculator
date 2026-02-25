# app/exceptions.py

class CalculatorError(Exception):
    """Base exception class for calculator errors."""
    pass


class OperationError(CalculatorError):
    """Raised when an invalid operation is requested."""
    pass


class ValidationError(CalculatorError):
    """Raised when user input fails validation."""
    pass


class HistoryError(CalculatorError):
    """Raised when undo/redo operations fail."""
    pass