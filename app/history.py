# app/history.py

from app.calculator_memento import CalculatorMemento
from app.exceptions import HistoryError


class HistoryManager:
    """
    Manages calculation history with undo/redo functionality.
    """

    def __init__(self):
        self._history = []
        self._undo_stack = []
        self._redo_stack = []

    def add(self, calculation):
        """Add a new calculation and save state for undo."""
        self._undo_stack.append(CalculatorMemento(self._history))
        self._history.append(calculation)
        self._redo_stack.clear()

    def get_history(self):
        return list(self._history)

    def clear(self):
        """Clear entire history."""
        self._undo_stack.append(CalculatorMemento(self._history))
        self._history.clear()
        self._redo_stack.clear()

    def undo(self):
        if not self._undo_stack:
            raise HistoryError("Nothing to undo.")

        self._redo_stack.append(CalculatorMemento(self._history))
        memento = self._undo_stack.pop()
        self._history = memento.get_state()

    def redo(self):
        if not self._redo_stack:
            raise HistoryError("Nothing to redo.")

        self._undo_stack.append(CalculatorMemento(self._history))
        memento = self._redo_stack.pop()
        self._history = memento.get_state()