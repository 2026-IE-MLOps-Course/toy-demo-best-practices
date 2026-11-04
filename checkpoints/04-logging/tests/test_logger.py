import logging

import pytest

from src.logger import configure_logging


def test_unknown_log_level_raises(tmp_path):
    with pytest.raises(ValueError, match="Unknown log level"):
        configure_logging(level="LOUD", log_file=tmp_path / "x.log")


def test_logger_writes_to_file(tmp_path):
    log_file = tmp_path / "logs" / "pipeline.log"
    configure_logging(level="INFO", log_file=log_file)
    logging.getLogger("demo").info("hello %s", "file")
    logging.shutdown()
    assert "hello file" in log_file.read_text(encoding="utf-8")
