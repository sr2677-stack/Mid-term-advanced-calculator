# app/main.py

from app.calculator import Calculator, LoggingObserver, AutoSaveObserver
from app.input_validators import validate_number
from app.exceptions import CalculatorError


def print_help():
    print("\nAvailable Commands:")
    print(" add a b")
    print(" subtract a b")
    print(" multiply a b")
    print(" divide a b")
    print(" power a b")
    print(" root a b")
    print(" modulus a b")
    print(" int_divide a b")
    print(" percent a b")
    print(" abs_diff a b")
    print(" history")
    print(" clear")
    print(" undo")
    print(" redo")
    print(" save")
    print(" load")
    print(" help")
    print(" exit\n")


def repl():
    calculator = Calculator()

    # Register observers
    calculator.register_observer(LoggingObserver())
    calculator.register_observer(AutoSaveObserver())

    print("Advanced Calculator (Type 'help' for commands)")

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
            elif command == "help":
                print_help()

            # History
            elif command == "history":
                history = calculator.get_history()
                if not history:
                    print("No history available.")
                for calc in history:
                    print(f"{calc.operation} {calc.a} {calc.b} = {calc.result}")

            # Clear
            elif command == "clear":
                calculator.clear_history()
                print("History cleared.")

            # Undo
            elif command == "undo":
                calculator.undo()
                print("Undo successful.")

            # Redo
            elif command == "redo":
                calculator.redo()
                print("Redo successful.")

            # Save
            elif command == "save":
                calculator.save_history()
                print("History saved.")

            # Load
            elif command == "load":
                calculator.load_history()
                print("History loaded.")

            # Operations
            else:
                if len(parts) != 3:
                    print("Invalid format. Use: operation a b")
                    continue

                a = validate_number(parts[1])
                b = validate_number(parts[2])

                result = calculator.calculate(command, a, b)
                print(f"Result: {result}")

        except CalculatorError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    repl()