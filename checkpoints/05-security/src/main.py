"""Run the configured pipeline: python -m src.main"""

import json
import logging
import os
from pathlib import Path

from dotenv import load_dotenv

from src.clean_data import clean_data
from src.config import load_config
from src.load_data import load_data
from src.logger import configure_logging
from src.model import accuracy, predict
from src.validate import validate, validate_schema

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def run():
    cfg = load_config(PROJECT_ROOT / "config.yaml")
    paths, data_cfg, gate = cfg["paths"], cfg["data"], cfg["quality_gate"]
    configure_logging(
        level=cfg["logging"]["level"], log_file=PROJECT_ROOT / paths["log_file"]
    )
    load_dotenv(PROJECT_ROOT / ".env")
    api_key = os.getenv("TRACKING_API_KEY")
    df = load_data(PROJECT_ROOT / paths["raw_data"])
    validate_schema(df, data_cfg["required_columns"])
    df = clean_data(df, data_cfg["feature"])
    validate(df, data_cfg["required_columns"], data_cfg["feature"])
    preds = predict(df[data_cfg["feature"]], cfg["model"]["usage_threshold"])
    score = accuracy(df[data_cfg["target"]], preds)
    passed = bool(score >= gate["min_value"])
    logger.info(
        "Quality gate %s: %s = %.3f (minimum %.2f)",
        "met" if passed else "NOT met",
        gate["metric"],
        score,
        gate["min_value"],
    )
    metrics = {gate["metric"]: score, "gate_met": passed, "rows": len(df)}
    report_path = PROJECT_ROOT / paths["report"]
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    logger.info("Report written to %s", report_path.relative_to(PROJECT_ROOT))
    if api_key:
        logger.info("Tracking key found: metrics would be sent to the tracker")
    else:
        logger.warning(
            "TRACKING_API_KEY not set: copy .env.example to .env to enable tracking"
        )
    return metrics


def main():
    """Exit 1 on an exception or a failed quality gate; keep the report either way."""
    try:
        metrics = run()
    except Exception:
        logger.exception("Pipeline failed")
        raise SystemExit(1)
    if not metrics["gate_met"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
