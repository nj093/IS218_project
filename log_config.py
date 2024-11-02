import logging
from config import Config

def setup_logging():
    log_level = Config.get("LOG_LEVEL", "INFO").upper()
    logging.basicConfig(level=log_level, format="%(asctime)s - %(levelname)s - %(message)s")

setup_logging()
