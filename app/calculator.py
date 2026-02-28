# app/calculator.py

import os
import pandas as pd
from app.operations import OperationFactory
from app.history import HistoryManager
from app.calculation import Calculation
from app.logger import CalculatorLogger
from app.calculator_config import Config
from app.exceptions import OperationError


class Calculator:
    """
    Main Calculator class.
    Coordinates operations, history management, and observers.
    """

    def __init__(self):
        self.history_manager = HistoryManager()
        self._observers = []
        self.logger = CalculatorLogger.setup_logger()

        Config.create_directories()

    # --------------------------
    # Observer Pattern
    # --------------------------

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, calculation):
        for observer in self._observers:
            observer.update(calculation)

    # --------------------------
    # Core Calculation
    # --------------------------

    def calculate(self, operation_name: str, a: float, b: float) -> float:
        operation = OperationFactory.create_operation(operation_name)
        result = operation.execute(a, b)

        calculation = Calculation(operation_name, a, b, result)
        self.history_manager.add(calculation)

        self.logger.info(
            f"{operation_name} | {a}, {b} = {result}"
        )

        self.notify_observers(calculation)

        return result

    # --------------------------
    # History Controls
    # --------------------------

    def get_history(self):
        return self.history_manager.get_history()

    def undo(self):
        self.history_manager.undo()

    def redo(self):
        self.history_manager.redo()

    def clear_history(self):
        self.history_manager.clear()

    # --------------------------
    # CSV Persistence
    # --------------------------

    def save_history(self):
        history = self.get_history()
        if not history:
            return

        file_path = os.path.join(Config.HISTORY_DIR, Config.HISTORY_FILE)

        df = pd.DataFrame([calc.to_dict() for calc in history])
        df.to_csv(file_path, index=False)

    def load_history(self):
        file_path = os.path.join(Config.HISTORY_DIR, Config.HISTORY_FILE)

        if not os.path.exists(file_path):
            raise OperationError("History file does not exist.")

        df = pd.read_csv(file_path)

        self.history_manager.clear()

        for _, row in df.iterrows():
            calc = Calculation.from_dict(row)
            self.history_manager.add(calc)


# ===============================
# Observers
# ===============================

class LoggingObserver:
    def __init__(self):
        self.logger = CalculatorLogger.setup_logger()

    def update(self, calculation):
        self.logger.info(
            f"[Observer] {calculation.operation} "
            f"{calculation.a}, {calculation.b} = {calculation.result}"
        )


class AutoSaveObserver:
    def update(self, calculation):
        file_path = os.path.join(Config.HISTORY_DIR, Config.HISTORY_FILE)

        df = pd.DataFrame([calculation.to_dict()])

        if os.path.exists(file_path):
            df.to_csv(file_path, mode="a", header=False, index=False)
        else:
            df.to_csv(file_path, index=False)