"""Run the configured pipeline: python -m src.main"""

import json
from pathlib import Path

from src.clean_data import clean_data
from src.config import load_config
from src.load_data import load_data
from src.model import accuracy, predict
from src.validate import validate, validate_schema

PROJECT_ROOT = Path(__file__).resolve().parents[1]
TRACKING_API_KEY = "sk-live-4f9a2c7e1b8d4a6f9c3e2b1a7d5f8e0c"  # Synthetic, never valid


def run():
    cfg = load_config(PROJECT_ROOT / "config.yaml")
    paths, data_cfg, gate = cfg["paths"], cfg["data"], cfg["quality_gate"]
    df = load_data(PROJECT_ROOT / paths["raw_data"])
    validate_schema(df, data_cfg["required_columns"])
    df = clean_data(df, data_cfg["feature"])
    validate(df, data_cfg["required_columns"], data_cfg["feature"])
    preds = predict(df[data_cfg["feature"]], cfg["model"]["usage_threshold"])
    score = accuracy(df[data_cfg["target"]], preds)
    passed = bool(score >= gate["min_value"])
    print("accuracy:", score)
    print("quality gate met" if passed else "quality gate NOT met")
    metrics = {gate["metric"]: score, "gate_met": passed, "rows": len(df)}
    report_path = PROJECT_ROOT / paths["report"]
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    print("sending metrics with key", TRACKING_API_KEY)
    return metrics


if __name__ == "__main__":
    run()
