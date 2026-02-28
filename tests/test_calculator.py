import os
import pytest
from app.calculator import Calculator, LoggingObserver, AutoSaveObserver
from app.exceptions import OperationError
from app.calculator_config import Config


def test_calculate_add():
    calc = Calculator()
    result = calc.calculate("add", 2, 3)
    assert result == 5
    assert len(calc.get_history()) == 1


def test_undo():
    calc = Calculator()
    calc.calculate("add", 2, 3)
    calc.undo()
    assert len(calc.get_history()) == 0


def test_redo():
    calc = Calculator()
    calc.calculate("add", 2, 3)
    calc.undo()
    calc.redo()
    assert len(calc.get_history()) == 1


def test_save_and_load_history():
    calc = Calculator()
    calc.calculate("add", 1, 1)
    calc.save_history()

    new_calc = Calculator()
    new_calc.load_history()

    assert len(new_calc.get_history()) == 1


def test_load_missing_file():
    calc = Calculator()

    # Remove file if exists
    file_path = os.path.join(Config.HISTORY_DIR, Config.HISTORY_FILE)
    if os.path.exists(file_path):
        os.remove(file_path)

    with pytest.raises(OperationError):
        calc.load_history()


def test_observer_registration():
    calc = Calculator()
    observer = LoggingObserver()

    calc.register_observer(observer)
    calc.calculate("add", 3, 4)

    assert len(calc.get_history()) == 1