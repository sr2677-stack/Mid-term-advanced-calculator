import builtins

from app import main


class DummyObserver:
    def update(self, calculation):
        return None


class DummyCalculation:
    def __init__(self, operation, a, b, result):
        self.operation = operation
        self.a = a
        self.b = b
        self.result = result


class DummyCalculator:
    def __init__(self):
        self.history = [DummyCalculation("add", 1.0, 2.0, 3.0)]
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = []

    def undo(self):
        return None

    def redo(self):
        return None

    def save_history(self):
        return None

    def load_history(self):
        return None

    def calculate(self, operation_name, a, b):
        if operation_name == "boom":
            raise RuntimeError("boom")
        return a + b


def test_repl_covers_command_paths(monkeypatch, capsys):
    commands = iter(
        [
            "",
            "help",
            "history",
            "clear",
            "history",
            "undo",
            "redo",
            "save",
            "load",
            "add 1",
            "add 2 3",
            "add x 2",
            "boom 1 2",
            "exit",
        ]
    )

    monkeypatch.setattr(main, "Calculator", DummyCalculator)
    monkeypatch.setattr(main, "LoggingObserver", DummyObserver)
    monkeypatch.setattr(main, "AutoSaveObserver", DummyObserver)
    monkeypatch.setattr(
        main.OperationFactory,
        "get_available_operations",
        lambda: ["add", "subtract", "power"],
    )
    monkeypatch.setattr(builtins, "input", lambda _: next(commands))

    main.repl()

    output = capsys.readouterr().out
    assert "Advanced Calculator" in output
    assert "Available Operations:" in output
    assert "Calculation History:" in output
    assert "History cleared." in output
    assert "No history available." in output
    assert "Undo successful." in output
    assert "Redo successful." in output
    assert "History saved." in output
    assert "History loaded." in output
    assert "Invalid format. Use: operation a b" in output
    assert "Result: 5.0" in output
    assert "Error: Input must be a numeric value." in output
    assert "Unexpected error: boom" in output
    assert "Exiting calculator." in output
