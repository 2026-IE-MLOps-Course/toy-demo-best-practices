from unittest.mock import Mock

import pandas as pd
import pytest

from src import main as pipeline


def test_invalid_data_stops_before_prediction(monkeypatch, capsys):
    bad = pd.DataFrame({"customer_id": [1], "usage_hours": [-1.0], "churned": [0]})
    monkeypatch.setattr(pipeline, "load_data", lambda path: bad)
    predict = Mock()
    monkeypatch.setattr(pipeline, "predict", predict)
    with pytest.raises(SystemExit) as exc:
        pipeline.main()
    assert exc.value.code == 1
    predict.assert_not_called()
    error = capsys.readouterr().err
    assert "Pipeline stopped:" in error
    assert "fix the source data" in error
    assert "Traceback" not in error


def test_success_completes_normally(monkeypatch):
    run = Mock(return_value=0.9)
    monkeypatch.setattr(pipeline, "run", run)
    pipeline.main()
    run.assert_called_once_with()


def test_unexpected_error_remains_visible(monkeypatch):
    monkeypatch.setattr(pipeline, "run", Mock(side_effect=RuntimeError("bug")))
    with pytest.raises(RuntimeError, match="bug"):
        pipeline.main()
