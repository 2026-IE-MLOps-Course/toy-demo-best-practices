import logging
from pathlib import Path

LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"


def configure_logging(level: str, log_file: Path) -> None:
    log_file.parent.mkdir(parents=True, exist_ok=True)
    formatter = logging.Formatter(LOG_FORMAT, datefmt="%Y-%m-%d %H:%M:%S")
    console = logging.StreamHandler()
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    for handler in (console, file_handler):
        handler.setFormatter(formatter)
    logging.basicConfig(level=level, handlers=[console, file_handler], force=True)
