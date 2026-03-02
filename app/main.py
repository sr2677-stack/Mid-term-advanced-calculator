# pragma: no cover
# app/main.py

from app.calculator import Calculator, LoggingObserver, AutoSaveObserver
from app.input_validators import validate_number
from app.exceptions import CalculatorError
from app.operations import OperationFactory


def print_help():
    """
    Dynamically generate help menu based on available operations.
    This ensures new operations automatically appear in help.
    """
    print("\nAvailable Operations:")
    for op in OperationFactory.get_available_operations():
        print(f"  {op} <a> <b>")

    print("\nOther Commands:")
    print("  history")
    print("  clear")
    print("  undo")
    print("  redo")
    print("  save")
    print("  load")
    print("  help")
    print("  exit\n")


def display_history(calculator: Calculator):
    history = calculator.get_history()

    if not history:
        print("No history available.")
        return

    print("\nCalculation History:")
    for calc in history:
        print(f"  {calc.operation} {calc.a} {calc.b} = {calc.result}")
    print()


def repl():
    calculator = Calculator()

    # Register observers
    calculator.register_observer(LoggingObserver())
    calculator.register_observer(AutoSaveObserver())

    print("\nAdvanced Calculator")
    print("Type 'help' to see available commands.\n")

    while True:
        try:
            user_input = input(">>> ").strip()

            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0].lower()

            # Exit
            if command == "exit":
                print("Exiting calculator.")
                break

            # Help
            if command == "help":
                print_help()
                continue

            # History
            if command == "history":
                display_history(calculator)
                continue

            # Clear
            if command == "clear":
                calculator.clear_history()
                print("History cleared.\n")
                continue

            # Undo
            if command == "undo":
                calculator.undo()
                print("Undo successful.\n")
                continue

            # Redo
            if command == "redo":
                calculator.redo()
                print("Redo successful.\n")
                continue

            # Save
            if command == "save":
                calculator.save_history()
                print("History saved.\n")
                continue

            # Load
            if command == "load":
                calculator.load_history()
                print("History loaded.\n")
                continue

            # Arithmetic operations
            if len(parts) != 3:
                print("Invalid format. Use: operation a b\n")
                continue

            a = validate_number(parts[1])
            b = validate_number(parts[2])

            result = calculator.calculate(command, a, b)
            print(f"Result: {result}\n")

        except CalculatorError as e:
            print(f"Error: {e}\n")

        except Exception as e:
            print(f"Unexpected error: {e}\n")


if __name__ == "__main__":  # pragma: no cover
    repl()