"""2.1 Error handling: every raise has a test that triggers it."""

import pytest

from src.validate import validate

COLUMNS = ["customer_id", "usage_hours", "churned"]


def test_valid_data_passes(df_ok):
    assert validate(df_ok, COLUMNS, "usage_hours") is True


def test_missing_column_raises(df_ok):
    with pytest.raises(ValueError, match="Missing required columns"):
        validate(df_ok.drop(columns="churned"), COLUMNS, "usage_hours")


def test_empty_data_raises(df_ok):
    with pytest.raises(ValueError, match="No rows"):
        validate(df_ok.iloc[0:0], COLUMNS, "usage_hours")


def test_negative_usage_raises(df_ok):
    df_ok.loc[0, "usage_hours"] = -1.0
    with pytest.raises(ValueError, match="negative usage_hours"):
        validate(df_ok, COLUMNS, "usage_hours")
    assert df_ok.loc[0, "usage_hours"] == -1.0
