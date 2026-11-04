"""Configure logging once, in main.py. Every other module only calls getLogger."""

import logging
import sys

LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"


def configure_logging(*, level, log_file):
    """Send every log line to the console and to a file, in one format."""
    numeric_level = getattr(logging, level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Unknown log level in config.yaml: {level}")
    log_file.parent.mkdir(parents=True, exist_ok=True)
    formatter = logging.Formatter(LOG_FORMAT, datefmt="%Y-%m-%d %H:%M:%S")

    console = logging.StreamHandler(sys.stdout)
    file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
    for handler in (console, file_handler):
        handler.setFormatter(formatter)

    logging.basicConfig(
        level=numeric_level, handlers=[console, file_handler], force=True
    )
