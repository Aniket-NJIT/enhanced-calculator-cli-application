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