import pytest
import os
import pandas as pd
from app.history import HistoryManager
from app.calculator_config import Config

@pytest.fixture
def history_manager(tmp_path):
    # Override the config to use a temporary directory for tests
    Config.HISTORY_FILE = os.path.join(tmp_path, "test_history.csv")
    Config.AUTO_SAVE = False  # Disable auto-save for pure history logic tests
    return HistoryManager()

def test_add_record(history_manager):
    history_manager.add_record("add", 5, 5, 10)
    assert len(history_manager.history) == 1
    assert history_manager.history[0]["operation"] == "add"

def test_undo_redo(history_manager):
    history_manager.add_record("add", 1, 1, 2)
    history_manager.add_record("subtract", 5, 2, 3)
    
    # State has 2 records. Undo should take us back to 1.
    assert history_manager.undo() is True
    assert len(history_manager.history) == 1
    assert history_manager.history[0]["operation"] == "add"
    
    # Redo should bring back the subtract record.
    assert history_manager.redo() is True
    assert len(history_manager.history) == 2
    assert history_manager.history[1]["operation"] == "subtract"

def test_empty_undo_redo(history_manager):
    assert history_manager.undo() is False
    assert history_manager.redo() is False

def test_clear_history(history_manager):
    history_manager.add_record("add", 1, 1, 2)
    history_manager.clear()
    assert len(history_manager.history) == 0
    # ensure clear can be undone
    history_manager.undo()
    assert len(history_manager.history) == 1

def test_save_and_load_csv(history_manager):
    history_manager.add_record("multiply", 3, 3, 9)
    history_manager.add_record("divide", 10, 2, 5)
    
    # Save
    assert history_manager.save_to_csv() is True
    assert os.path.exists(Config.HISTORY_FILE)
    
    # Clear and Load
    history_manager.clear()
    assert len(history_manager.history) == 0
    
    count = history_manager.load_from_csv()
    assert count == 2
    assert history_manager.history[0]["operation"] == "multiply"

def test_load_nonexistent_csv(history_manager):
    with pytest.raises(FileNotFoundError):
        history_manager.load_from_csv()