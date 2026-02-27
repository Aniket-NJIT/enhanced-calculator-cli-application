import sys
import logging
from colorama import init, Fore, Style
from app.calculator_config import Config
from app.operations import OperationFactory
from app.history import HistoryManager, auto_save_observer
from app.exceptions import CalculatorException

# Initialize Colorama
init(autoreset=True)

class CalculatorApp:
    def __init__(self):
        Config.ensure_dirs()
        self.setup_logging()
        self.history_manager = HistoryManager()
        self.history_manager.add_observer(auto_save_observer)
        self.history_manager.add_observer(self.logging_observer)

    def setup_logging(self):
        logging.basicConfig(
            filename=Config.LOG_FILE,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def logging_observer(self, action_type, record):
        self.logger.info(f"Action: {action_type} | Record: {record}")

    def run(self):
        print(Fore.CYAN + Style.BRIGHT + "=== Advanced Calculator REPL ===")
        print(Fore.CYAN + "Type 'help' for commands or 'exit' to quit.")
        
        while True:
            try:
                user_input = input(Fore.YELLOW + "calc> " + Style.RESET_ALL).strip().split()
                if not user_input: continue
                
                command = user_input[0].lower()
                
                if command == "exit":
                    print(Fore.CYAN + "Exiting. Goodbye!")
                    sys.exit(0)
                elif command == "help":
                    print(Fore.GREEN + "Commands: add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff [num1] [num2]")
                    print(Fore.GREEN + "State: undo, redo, history, clear")
                elif command == "undo":
                    if self.history_manager.undo():
                        print(Fore.GREEN + "Undo successful.")
                    else:
                        print(Fore.RED + "Nothing to undo.")
                elif command == "redo":
                    if self.history_manager.redo():
                        print(Fore.GREEN + "Redo successful.")
                    else:
                        print(Fore.RED + "Nothing to redo.")
                elif command == "history":
                    for idx, record in enumerate(self.history_manager.history):
                        print(Fore.MAGENTA + f"{idx}: {record['operation']} -> {record['result']}")
                elif command == "clear":
                    self.history_manager.clear()
                    print(Fore.GREEN + "History cleared.")
                elif command == "save":
                    if self.history_manager.save_to_csv():
                        print(Fore.GREEN + f"History saved to {Config.HISTORY_FILE}.")
                    else:
                        print(Fore.RED + "History is empty. Nothing to save.")
                elif command == "load":
                    try:
                        count = self.history_manager.load_from_csv()
                        print(Fore.GREEN + f"Loaded {count} records from history.")
                    except FileNotFoundError as e:
                        print(Fore.RED + str(e))
                else:
                    # Assume it's an arithmetic operation
                    if len(user_input) != 3:
                        print(Fore.RED + "Usage: <operation> <num1> <num2>")
                        continue
                    
                    a, b = float(user_input[1]), float(user_input[2])
                    op = OperationFactory.get_operation(command)
                    result = op.execute(a, b)
                    result = round(result, Config.PRECISION)
                    
                    self.history_manager.add_record(command, a, b, result)
                    print(Fore.GREEN + Style.BRIGHT + f"Result: {result}")
                    
            except ValueError:
                print(Fore.RED + "Error: Operands must be numbers.")
                self.logger.error("Value error: Operands must be numbers.")
            except CalculatorException as e:
                print(Fore.RED + f"Error: {str(e)}")
                self.logger.error(f"Calculator Error: {str(e)}")
            except Exception as e:
                print(Fore.RED + f"Unexpected Error: {str(e)}")
                self.logger.critical(f"Unexpected Error: {str(e)}")

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()