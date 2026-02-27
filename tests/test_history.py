import pytest
from app.history import HistoryManager
from app.calculation import Calculation
from app.exceptions import HistoryError


def test_add_history():
    history = HistoryManager()
    calc = Calculation("add", 1, 2, 3)
    history.add(calc)

    assert len(history.get_history()) == 1


def test_undo():
    history = HistoryManager()
    calc = Calculation("add", 1, 2, 3)
    history.add(calc)

    history.undo()
    assert len(history.get_history()) == 0


def test_redo():
    history = HistoryManager()
    calc = Calculation("add", 1, 2, 3)
    history.add(calc)

    history.undo()
    history.redo()

    assert len(history.get_history()) == 1


def test_undo_empty():
    history = HistoryManager()

    with pytest.raises(HistoryError):
        history.undo()


def test_redo_empty():
    history = HistoryManager()

    with pytest.raises(HistoryError):
        history.redo()