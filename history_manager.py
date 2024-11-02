import pandas as pd
import os
from config import Config

class HistoryManager:
    def __init__(self):
        self.history_file = Config.get("HISTORY_FILE", "history.csv")
        self.history = pd.DataFrame(columns=["operation", "a", "b", "result"])

    def log_calculation(self, operation, a, b, result):
        self.history = pd.concat([self.history, pd.DataFrame([{
            "operation": operation,
            "a": a,
            "b": b,
            "result": result
        }])], ignore_index=True)

    def save_history(self):
        self.history.to_csv(self.history_file, index=False)

    def load_history(self):
        if os.path.exists(self.history_file):
            self.history = pd.read_csv(self.history_file)

    def clear_history(self):
        self.history = pd.DataFrame(columns=["operation", "a", "b", "result"])
        if os.path.exists(self.history_file):
            os.remove(self.history_file)
