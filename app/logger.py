# app/logger.py

import logging
import os
from app.calculator_config import Config


class CalculatorLogger:
    """Handles logging configuration for the calculator."""

    @staticmethod
    def setup_logger():
        Config.create_directories()

        log_path = os.path.join(Config.LOG_DIR, Config.LOG_FILE)

        logger = logging.getLogger("CalculatorLogger")
        logger.setLevel(logging.INFO)

        if not logger.handlers:
            file_handler = logging.FileHandler(log_path)
            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger