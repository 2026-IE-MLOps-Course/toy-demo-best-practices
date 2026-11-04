import logging
from pathlib import Path

import pandas as pd

from src.clean_data import clean_data
from src.load_data import load_data


def test_clean_drops_missing_and_warns(caplog):
    df = pd.DataFrame({"usage_hours": [1.0, None, 3.0]})
    with caplog.at_level(logging.WARNING):
        cleaned = clean_data(df, "usage_hours")
    assert len(cleaned) == 2
    assert "Dropped 1 row(s)" in caplog.text


def test_clean_is_silent_when_nothing_dropped(caplog):
    with caplog.at_level(logging.WARNING):
        clean_data(pd.DataFrame({"usage_hours": [1.0]}), "usage_hours")
    assert caplog.text == ""


def test_load_logs_row_count(caplog):
    with caplog.at_level(logging.INFO):
        load_data(Path("data/raw/customers.csv"))
    assert "Loaded 12 rows from customers.csv" in caplog.text


def test_load_returns_all_rows():
    assert len(load_data(Path("data/raw/customers.csv"))) == 12
