"""Integration: run the whole pipeline on a copy of the project in tmp_path."""

import json
import shutil
from pathlib import Path

import pytest

import src.main as pipeline

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def project(tmp_path, monkeypatch):
    shutil.copy(ROOT / "config.yaml", tmp_path / "config.yaml")
    shutil.copytree(ROOT / "data" / "raw", tmp_path / "data" / "raw")
    monkeypatch.setattr(pipeline, "PROJECT_ROOT", tmp_path)
    monkeypatch.delenv("TRACKING_API_KEY", raising=False)
    return tmp_path


def test_run_end_to_end_writes_report(project):
    metrics = pipeline.run()
    assert metrics["gate_met"] is True
    assert (project / "reports" / "metrics.json").exists()


def test_main_exits_with_code_1_on_bad_data(project):
    config = project / "config.yaml"
    config.write_text(config.read_text().replace("customers.csv", "customers_bad.csv"))
    with pytest.raises(SystemExit) as exit_info:
        pipeline.main()
    assert exit_info.value.code == 1


def test_failed_quality_gate_exits_1_but_keeps_report(project):
    config = project / "config.yaml"
    config.write_text(
        config.read_text().replace("usage_threshold: 10.0", "usage_threshold: 3.0")
    )
    with pytest.raises(SystemExit) as exit_info:
        pipeline.main()
    assert exit_info.value.code == 1
    metrics = json.loads((project / "reports" / "metrics.json").read_text())
    assert metrics["gate_met"] is False
    assert metrics["accuracy"] == pytest.approx(7 / 11)


def test_missing_feature_fails_before_cleaning(project):
    raw = project / "data" / "raw" / "customers.csv"
    raw.write_text(raw.read_text().replace("usage_hours", "wrong_column"))
    with pytest.raises(ValueError, match="Missing required columns.*usage_hours"):
        pipeline.run()


def test_missing_config_is_reported_by_main(project):
    (project / "config.yaml").unlink()
    with pytest.raises(SystemExit) as exit_info:
        pipeline.main()
    assert exit_info.value.code == 1
