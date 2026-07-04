"""
logging_config.py

Centralized logging configuration for the Trading Bot.

This module configures:

1. Console logging (INFO and above)
2. File logging (DEBUG and above)

Usage:
    from bot.logging_config import setup_logger

    logger = setup_logger(__name__)
"""

import logging
from pathlib import Path


# -------------------------------------------------------------------
# Log File Location
# -------------------------------------------------------------------

LOG_FILE = Path("trading_bot.log")


# -------------------------------------------------------------------
# Logger Factory
# -------------------------------------------------------------------

def setup_logger(name: str) -> logging.Logger:
    """
    Create and return a configured logger.

    Parameters
    ----------
    name : str
        Usually __name__

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """

    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    # -------------------------------------------------------------
    # Formatter
    # Example:
    # 2025-07-04 19:30:20 | INFO | orders | Order submitted
    # -------------------------------------------------------------

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # -------------------------------------------------------------
    # Console Handler
    # -------------------------------------------------------------

    console_handler = logging.StreamHandler()

    console_handler.setLevel(logging.INFO)

    console_handler.setFormatter(formatter)

    # -------------------------------------------------------------
    # File Handler
    # -------------------------------------------------------------

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )

    file_handler.setLevel(logging.DEBUG)

    file_handler.setFormatter(formatter)

    # -------------------------------------------------------------
    # Attach Handlers
    # -------------------------------------------------------------

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.propagate = False

    return logger