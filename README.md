# Advanced Python Calculator

An advanced command-line calculator application built with Python. It features various arithmetic operations, a REPL (Read-Eval-Print Loop) interface, and robust error handling. 

This project heavily utilizes Object-Oriented Programming (OOP) principles and classic GoF Design Patterns (Factory, Memento, Observer). Data persistence is handled via `pandas`, and the application is fully covered by a `pytest` suite enforced by GitHub Actions CI/CD.

## Features
* **Advanced Math Operations**: Addition, Subtraction, Multiplication, Division, Power, Root, Modulus, Integer Division, Percentage, and Absolute Difference.
* **Design Patterns**: 
  * **Factory Pattern**: for operation generation.
  * **Memento Pattern**: for robust `undo` and `redo` history states.
  * **Observer Pattern**: for auto-saving and logging events.
* **Data Persistence**: Uses `pandas` to save and load calculation history to/from a CSV file.
* **Bonus - Color-Coded Outputs**: Utilizes `colorama` for a beautiful, readable REPL interface.

## Installation Instructions

1. **Clone the repository:**
```bash
    git clone https://github.com/Aniket-NJIT/enhanced-calculator-cli-application.git
    cd enhanced-calculator-cli-application
```

2. **Set up the virtual environment:**
```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. **Install dependencies:**
```bash
   pip install -r requirements.txt 
```

## Configuration Setup
Create a `.env` file in the root directory based on the following variables. The application uses `python-dotenv` to load these on startup.
```bash
    CALCULATOR_LOG_DIR=logs
    CALCULATOR_HISTORY_DIR=history
    CALCULATOR_MAX_HISTORY_SIZE=100
    CALCULATOR_AUTO_SAVE=true
    CALCULATOR_HISTORY_FILE=history/history.csv
    CALCULATOR_LOG_FILE=logs/calculator.log
    CALCULATOR_PRECISION=4
    CALCULATOR_MAX_INPUT_VALUE=1000000000
    CALCULATOR_DEFAULT_ENCODING=utf-8
```

## Usage Guide
To start the calculator's REPL interface, run:
```bash
    python -m app.calculator
```

### Supported Commands
* **Math operations**: add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff
    * **Syntax**: `<command> <number1> <number2>` (e.g., add 5 10)

* **History Management**:
    * `history`: View past calculations.
    * `clear`: Wipe history.
    * `undo`: Revert the last operation.
    * `redo`: Remake the last undone operation.

* **Data Persistence**:
    * `save`: Manually save history to CSV via Pandas.
    * `load`: Manually load history from CSV via Pandas.

* **System**: help, exit

## Testing & Coverage
This project uses `pytest` and `pytest-cov` to ensure a minimum of 90% code coverage.

To run the tests and view the coverage report:
```bash
    pytest --cov=app --cov-report=term-missing
```

## CI/CD Pipeline
This project includes a `.github/workflows/python-app.yml` file. On every push or pull request to the main branch, GitHub Actions will automatically set up the Python environment, install dependencies, run the test suite, and enforce the 90% coverage threshold. If coverage drops below 90%, the build will fail.