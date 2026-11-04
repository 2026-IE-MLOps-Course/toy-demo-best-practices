"""Configuration rejects missing files, sections and keys."""

from pathlib import Path

import pytest
import yaml

from src.config import load_config


def test_missing_config_file_raises(tmp_path):
    with pytest.raises(FileNotFoundError):
        load_config(tmp_path / "config.yaml")


def test_missing_section_raises(tmp_path):
    path = tmp_path / "config.yaml"
    path.write_text("paths: {}\n", encoding="utf-8")
    with pytest.raises(KeyError, match="missing sections"):
        load_config(path)


def test_missing_key_raises(tmp_path):
    reference = Path(__file__).resolve().parents[1] / "config.yaml"
    cfg = yaml.safe_load(reference.read_text(encoding="utf-8"))
    del cfg["paths"]["raw_data"]
    path = tmp_path / "config.yaml"
    path.write_text(yaml.safe_dump(cfg), encoding="utf-8")
    with pytest.raises(KeyError, match="missing keys"):
        load_config(path)
