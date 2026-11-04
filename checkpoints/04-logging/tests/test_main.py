import logging
from unittest.mock import Mock

import pytest

from src import main as pipeline


def test_expected_failure_logs_once_without_traceback(monkeypatch, caplog):
    error = ValueError("negative usage_hours; fix the source data")
    monkeypatch.setattr(pipeline, "run", Mock(side_effect=error))
    with caplog.at_level(logging.ERROR), pytest.raises(SystemExit) as exc:
        pipeline.main()
    assert exc.value.code == 1
    assert len(caplog.records) == 1
    assert "Pipeline stopped:" in caplog.text
    assert "fix the source data" in caplog.text
    assert caplog.records[0].exc_info is None


def test_success_completes_normally(monkeypatch):
    run = Mock(return_value=0.9)
    monkeypatch.setattr(pipeline, "run", run)
    pipeline.main()
    run.assert_called_once_with()


def test_unexpected_failure_keeps_traceback(monkeypatch, caplog):
    monkeypatch.setattr(pipeline, "run", Mock(side_effect=RuntimeError("bug")))
    with caplog.at_level(logging.ERROR), pytest.raises(SystemExit) as exc:
        pipeline.main()
    assert exc.value.code == 1
    assert len(caplog.records) == 1
    assert "Pipeline failed" in caplog.text
    assert caplog.records[0].exc_info[0] is RuntimeError
