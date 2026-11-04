import logging

from src.main import run
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


def test_run_reads_dotenv_without_exposing_secret(project, capsys, monkeypatch):
    monkeypatch.delenv("TRACKING_API_KEY", raising=False)
    secret = project.name  # A unique fake value, created only during the test
    (project / ".env").write_text(f"TRACKING_API_KEY={secret}\n", encoding="utf-8")
    assert run()["rows"] == 11
    logging.shutdown()
    output = capsys.readouterr().out
    log = (project / "logs" / "pipeline.log").read_text(encoding="utf-8")
    assert "Tracking key found" in output
    assert "Tracking key found" in log
    assert secret not in output + log


def test_run_warns_when_optional_secret_is_missing(project, capsys):
    run()
    assert "TRACKING_API_KEY not set" in capsys.readouterr().out
