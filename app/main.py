# app/main.py

from colorama import init, Fore, Style
from app.calculator import Calculator, LoggingObserver, AutoSaveObserver
from app.input_validators import validate_number
from app.exceptions import CalculatorError
from app.operations import OperationFactory

init(autoreset=True)


def print_help():
    """
    Dynamically generate help menu based on available operations.
    This ensures new operations automatically appear in help.
    """
    print(Fore.CYAN + "\nAvailable Operations:")
    for op in OperationFactory.get_available_operations():
        print(Fore.YELLOW + f"  {op} <a> <b>")

    print(Fore.CYAN + "\nOther Commands:")
    for cmd in ["history", "clear", "undo", "redo", "save", "load", "help", "exit"]:
        print(Fore.YELLOW + f"  {cmd}")
    print()


def display_history(calculator: Calculator):
    history = calculator.get_history()

    if not history:
        print(Fore.YELLOW + "No history available.")
        return

    print(Fore.CYAN + "\nCalculation History:")
    for calc in history:
        print(Fore.WHITE + f"  {calc.operation} {calc.a} {calc.b} = " + Fore.GREEN + f"{calc.result}")
    print()


def repl():
    calculator = Calculator()

    # Register observers
    calculator.register_observer(LoggingObserver())
    calculator.register_observer(AutoSaveObserver())

    print(Fore.CYAN + Style.BRIGHT + "\nAdvanced Calculator")
    print(Fore.WHITE + "Type 'help' to see available commands.\n")

    while True:
        try:
            user_input = input(Fore.WHITE + ">>> ").strip()

            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0].lower()

            if command == "exit":
                print(Fore.CYAN + "Exiting calculator.")
                break

            if command == "help":
                print_help()
                continue

            if command == "history":
                display_history(calculator)
                continue

            if command == "clear":
                calculator.clear_history()
                print(Fore.YELLOW + "History cleared.\n")
                continue

            if command == "undo":
                calculator.undo()
                print(Fore.YELLOW + "Undo successful.\n")
                continue

            if command == "redo":
                calculator.redo()
                print(Fore.YELLOW + "Redo successful.\n")
                continue

            if command == "save":
                calculator.save_history()
                print(Fore.YELLOW + "History saved.\n")
                continue

            if command == "load":
                calculator.load_history()
                print(Fore.YELLOW + "History loaded.\n")
                continue

            if len(parts) != 3:
                print(Fore.RED + "Invalid format. Use: operation a b\n")
                continue

            a = validate_number(parts[1])
            b = validate_number(parts[2])

            result = calculator.calculate(command, a, b)
            print(Fore.GREEN + f"Result: {result}\n")

        except CalculatorError as e:
            print(Fore.RED + f"Error: {e}\n")

        except Exception as e:
            print(Fore.RED + f"Unexpected error: {e}\n")


if __name__ == "__main__":  # pragma: no cover
    repl()