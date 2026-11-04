import pandas as pd
import pytest

from src.validate import validate

COLUMNS = ["customer_id", "usage_hours", "churned"]


def make_df(usage):
    return pd.DataFrame({"customer_id": [1], "usage_hours": [usage], "churned": [0]})


def test_valid_data_passes():
    assert validate(make_df(5.0), COLUMNS, "usage_hours") is True


def test_missing_column_raises():
    with pytest.raises(ValueError, match="Missing required columns"):
        validate(make_df(5.0).drop(columns="churned"), COLUMNS, "usage_hours")


def test_empty_data_raises():
    with pytest.raises(ValueError, match="No rows"):
        validate(make_df(5.0).iloc[0:0], COLUMNS, "usage_hours")


def test_negative_usage_raises():
    with pytest.raises(ValueError, match="negative usage_hours"):
        validate(make_df(-1.0), COLUMNS, "usage_hours")
