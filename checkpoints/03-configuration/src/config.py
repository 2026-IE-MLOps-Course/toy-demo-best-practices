"""Load settings and reject missing files, sections and keys."""

import yaml

REQUIRED_SECTIONS = ("paths", "data", "model", "quality_gate")
REQUIRED_KEYS = {
    "paths": ("raw_data", "report"),
    "data": ("required_columns", "feature", "target"),
    "model": ("usage_threshold",),
    "quality_gate": ("metric", "min_value"),
}


def load_config(path):
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")
    with path.open(encoding="utf-8") as handle:
        cfg = yaml.safe_load(handle) or {}
    missing = [section for section in REQUIRED_SECTIONS if section not in cfg]
    if missing:
        raise KeyError(f"config.yaml is missing sections: {missing}")
    for section, keys in REQUIRED_KEYS.items():
        missing = [key for key in keys if key not in cfg[section]]
        if missing:
            raise KeyError(
                f"config.yaml section '{section}' is missing keys: {missing}"
            )
    return cfg
