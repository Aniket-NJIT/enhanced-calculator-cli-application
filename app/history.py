import pandas as pd
from datetime import datetime
import os
from app.calculator_config import Config
from app.calculator_memento import HistoryMemento

class HistoryManager:
    def __init__(self):
        self.history = []
        self.undo_stack = []
        self.redo_stack = []
        self.observers = []
        
    def add_observer(self, observer_func):
        self.observers.append(observer_func)
        
    def _notify_observers(self, action_type, record):
        for obs in self.observers:
            obs(action_type, record)

    def save_state(self):
        self.undo_stack.append(HistoryMemento(self.history))
        self.redo_stack.clear()

    def add_record(self, operation: str, a: float, b: float, result: float):
        self.save_state()
        record = {
            "timestamp": datetime.now().isoformat(),
            "operation": operation,
            "operand_a": a,
            "operand_b": b,
            "result": result
        }
        self.history.append(record)
        if len(self.history) > Config.MAX_HISTORY:
            self.history.pop(0)
        self._notify_observers("calculation", record)

    def undo(self):
        if not self.undo_stack: return False
        self.redo_stack.append(HistoryMemento(self.history))
        memento = self.undo_stack.pop()
        self.history = memento.get_state()
        self._notify_observers("undo", {"timestamp": datetime.now().isoformat(), "operation": "undo"})
        return True

    def redo(self):
        if not self.redo_stack: return False
        self.undo_stack.append(HistoryMemento(self.history))
        memento = self.redo_stack.pop()
        self.history = memento.get_state()
        self._notify_observers("redo", {"timestamp": datetime.now().isoformat(), "operation": "redo"})
        return True

    def clear(self):
        self.save_state()
        self.history.clear()

    def save_to_csv(self):
        """Manually save the current history state to CSV using pandas."""
        if not self.history:
            return False
        df = pd.DataFrame(self.history)
        df.to_csv(Config.HISTORY_FILE, index=False)
        return True

    def load_from_csv(self):
        """Manually load history from CSV using pandas."""
        if not os.path.exists(Config.HISTORY_FILE):
            raise FileNotFoundError("History file does not exist.")
        df = pd.read_csv(Config.HISTORY_FILE)
        self.history = df.to_dict('records')
        return len(self.history)

def auto_save_observer(action_type, record):
    if not Config.AUTO_SAVE: return
    file_path = Config.HISTORY_FILE
    df_new = pd.DataFrame([record])
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        df_new.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df_new.to_csv(file_path, mode='w', header=True, index=False)