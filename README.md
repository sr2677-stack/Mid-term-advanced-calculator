# Advanced Calculator Application

## Project Description

This project is a command-line Advanced Calculator built in Python using the REPL (Read-Eval-Print Loop) pattern.

The application supports basic and advanced arithmetic operations, history management with undo/redo, CSV persistence, logging, configuration management, and robust error handling.

The system is modular, extensible, and built using multiple software design patterns to ensure clean architecture and maintainability.

---

## Design Patterns Implemented

### 1️⃣ Factory Pattern
- Implemented in `app/operations.py`
- Responsible for dynamic creation of operation instances
- Allows easy addition of new operations without modifying calculator logic

### 2️⃣ Memento Pattern
- Implemented in `app/calculator_memento.py` and `app/history.py`
- Enables undo and redo functionality
- Safely preserves calculator state snapshots

### 3️⃣ Observer Pattern
- Implemented in `app/calculator.py`
- `LoggingObserver` logs calculation activity
- `AutoSaveObserver` automatically persists history to CSV

### 4️⃣ Dynamic Help Feature (Optional Enhancement)
- Help menu dynamically reads available operations from the Factory
- Adding new operations automatically updates the help output
- Improves extensibility and reduces duplication

---

## Project Structure

```text
advanced_calculator/
├── app/
│   ├── __init__.py
│   ├── calculator.py
│   ├── calculation.py
│   ├── calculator_config.py
│   ├── calculator_memento.py
│   ├── exceptions.py
│   ├── history.py
│   ├── input_validators.py
│   ├── logger.py
│   ├── main.py
│   └── operations.py
├── tests/
├── .github/workflows/python-app.yml
├── requirements.txt
└── README.md
Installation Instructions

Clone the repository and move into the project directory.

Create and activate a virtual environment.

Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1
Linux/macOS
python3 -m venv venv
source venv/bin/activate

### Install Dependencies

pip install -r requirements.txt
Configuration Setup (.env)

The application loads configuration values using python-dotenv.

⚙️ Configuration (.env)

CALCULATOR_LOG_DIR=logs
CALCULATOR_HISTORY_DIR=data
CALCULATOR_MAX_HISTORY_SIZE=100
CALCULATOR_AUTO_SAVE=true
CALCULATOR_PRECISION=2
CALCULATOR_MAX_INPUT_VALUE=1000000
CALCULATOR_DEFAULT_ENCODING=utf-8
CALCULATOR_LOG_FILE=calculator.log
CALCULATOR_HISTORY_FILE=history.csv

If a variable is missing, default values from app/calculator_config.py are used.

Usage Guide (REPL)

Run the calculator:

python -m app.main
Supported Operation Commands

add a b

subtract a b

multiply a b

divide a b

power a b

root a b

modulus a b

int_divide a b

percent a b

abs_diff a b

Other Commands

history

clear

undo

redo

save

load

help

exit

Example session:

>>> add 2 3
Result: 5.0

>>> power 2 5
Result: 32.0

>>> history
add 2.0 3.0 = 5.0
power 2.0 5.0 = 32.0
Testing Instructions

🧪 Running Tests
pytest
Run tests with coverage report:
pytest --cov=app
Enforce minimum coverage threshold (90%):
pytest --cov=app --cov-fail-under=90

▶️ Running the Application

From the project root:
python -m app.main
