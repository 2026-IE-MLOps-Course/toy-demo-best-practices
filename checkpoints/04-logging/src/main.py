import logging
from pathlib import Path

from src.load_data import load_data
from src.clean_data import clean_data
from src.validate import validate
from src.model import predict, accuracy
from src.config import load_config
from src.logger import configure_logging

logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
TRACKING_API_KEY = "sk-live-4f9a2c7e1b8d4a6f9c3e2b1a7d5f8e0c"  # Synthetic, never valid


def run():
    cfg = load_config(PROJECT_ROOT / "config.yaml")
    configure_logging(cfg["logging"]["level"], PROJECT_ROOT / cfg["paths"]["log_file"])
    feature = cfg["data"]["feature"]
    df = load_data(PROJECT_ROOT / cfg["paths"]["raw_data"])
    df = clean_data(df, feature)
    validate(df, cfg["data"]["required_columns"], feature)
    threshold = cfg["model"]["usage_threshold"]
    logger.debug("Predicting with threshold %.1f", threshold)
    preds = predict(df[feature], threshold)
    score = accuracy(df[cfg["data"]["target"]], preds)
    gate = cfg["quality_gate"]
    if score >= gate["min_value"]:
        logger.info(
            "Quality gate met: %s = %.3f (minimum %.2f)",
            gate["metric"],
            score,
            gate["min_value"],
        )
    else:
        logger.warning(
            "Quality gate NOT met: %s = %.3f (minimum %.2f)",
            gate["metric"],
            score,
            gate["min_value"],
        )
    print("sending metrics with key", TRACKING_API_KEY)
    return score


def main():
    try:
        run()
    except (ValueError, OSError, KeyError) as exc:
        logger.error("Pipeline stopped: %s", exc)
        raise SystemExit(1) from None
    except Exception:
        logger.exception("Pipeline failed")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
