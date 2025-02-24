import logging
import os

class Logger:
    """Handles logging for debugging and tracking system behavior."""
    def __init__(self, log_file="logs/system.log"):
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        self.logger = logging.getLogger("PatientSchedulerLogger")

    def info(self, message):
        """Logs an informational message."""
        self.logger.info(message)

    def warning(self, message):
        """Logs a warning message."""
        self.logger.warning(message)

    def error(self, message):
        """Logs an error message."""
        self.logger.error(message)

    def debug(self, message):
        """Logs a debug message."""
        self.logger.debug(message)
