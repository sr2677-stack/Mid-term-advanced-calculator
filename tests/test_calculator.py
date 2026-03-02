import os
import pytest
from app.calculator import Calculator, LoggingObserver, AutoSaveObserver
from app.calculation import Calculation
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


def test_clear_history():
    calc = Calculator()
    calc.calculate("add", 4, 5)
    calc.clear_history()
    assert len(calc.get_history()) == 0


def test_save_history_no_entries_returns_early(tmp_path, monkeypatch):
    monkeypatch.setattr(Config, "HISTORY_DIR", str(tmp_path))
    calc = Calculator()

    calc.save_history()

    file_path = os.path.join(Config.HISTORY_DIR, Config.HISTORY_FILE)
    assert not os.path.exists(file_path)


def test_autosave_observer_creates_and_appends_file(tmp_path, monkeypatch):
    monkeypatch.setattr(Config, "HISTORY_DIR", str(tmp_path))
    observer = AutoSaveObserver()
    calc1 = Calculation("add", 1, 2, 3)
    calc2 = Calculation("multiply", 2, 3, 6)

    observer.update(calc1)
    observer.update(calc2)

    file_path = os.path.join(Config.HISTORY_DIR, Config.HISTORY_FILE)
    assert os.path.exists(file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    assert len(lines) == 3
