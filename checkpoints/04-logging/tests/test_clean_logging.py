"""2.4 Logging: caplog lets a test check that the right message was logged."""

import logging

import pandas as pd

from src.clean_data import clean_data


def test_clean_drops_missing_and_warns(caplog):
    df = pd.DataFrame({"usage_hours": [1.0, None, 3.0]})
    with caplog.at_level(logging.WARNING):
        cleaned = clean_data(df, "usage_hours")
    assert len(cleaned) == 2
    assert "Dropped 1 row(s)" in caplog.text


def test_clean_logs_nothing_when_nothing_dropped(caplog):
    with caplog.at_level(logging.WARNING):
        clean_data(pd.DataFrame({"usage_hours": [1.0]}), "usage_hours")
    assert caplog.text == ""
