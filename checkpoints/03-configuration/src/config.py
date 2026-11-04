from pathlib import Path

import yaml

REQUIRED_SECTIONS = ["paths", "data", "model", "quality_gate", "logging"]


def load_config(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        cfg = yaml.safe_load(handle) or {}
    missing = [s for s in REQUIRED_SECTIONS if s not in cfg]
    if missing:
        raise KeyError(f"config.yaml is missing sections: {missing}")
    return cfg
