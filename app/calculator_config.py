import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    LOG_DIR = os.getenv("CALCULATOR_LOG_DIR", "logs")
    HISTORY_DIR = os.getenv("CALCULATOR_HISTORY_DIR", "history")
    MAX_HISTORY = int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", "100"))
    AUTO_SAVE = os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true"
    HISTORY_FILE = os.getenv("CALCULATOR_HISTORY_FILE", "history/history.csv")
    LOG_FILE = os.getenv("CALCULATOR_LOG_FILE", "logs/calculator.log")
    PRECISION = int(os.getenv("CALCULATOR_PRECISION", "4"))
    
    @classmethod
    def ensure_dirs(cls):
        os.makedirs(cls.LOG_DIR, exist_ok=True)
        os.makedirs(cls.HISTORY_DIR, exist_ok=True)