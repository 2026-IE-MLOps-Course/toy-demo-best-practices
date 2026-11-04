import pytest

import src.main as pipeline


def test_schema_checked_before_cleaning(df_ok, monkeypatch):
    monkeypatch.setattr(
        pipeline, "load_data", lambda path: df_ok.drop(columns="usage_hours")
    )

    def must_not_clean(*args):
        pytest.fail("Cleaning must not run before the column check")

    monkeypatch.setattr(pipeline, "clean_data", must_not_clean)
    with pytest.raises(ValueError, match="Missing required columns"):
        pipeline.run()


def test_empty_data_stops_pipeline(df_ok, monkeypatch):
    monkeypatch.setattr(pipeline, "load_data", lambda path: df_ok.iloc[0:0])
    with pytest.raises(ValueError, match="No rows"):
        pipeline.run()
