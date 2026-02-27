# app/calculator_memento.py


class CalculatorMemento:
    """
    Memento class that stores calculator state.
    Used for undo/redo functionality.
    """

    def __init__(self, state):
        self._state = list(state)  # copy of history list

    def get_state(self):
        return list(self._state)