from pathlib import Path

from src.load_data import load_data
from src.clean_data import clean_data
from src.validate import validate
from src.model import predict, accuracy
from src.config import load_config

PROJECT_ROOT = Path(__file__).resolve().parents[1]
TRACKING_API_KEY = "sk-live-4f9a2c7e1b8d4a6f9c3e2b1a7d5f8e0c"  # Synthetic, never valid


def run():
    cfg = load_config(PROJECT_ROOT / "config.yaml")
    feature = cfg["data"]["feature"]
    df = load_data(PROJECT_ROOT / cfg["paths"]["raw_data"])
    df = clean_data(df)
    validate(df, cfg["data"]["required_columns"], feature)
    preds = predict(df[feature], cfg["model"]["usage_threshold"])
    score = accuracy(df[cfg["data"]["target"]], preds)
    print("accuracy:", score)
    if score >= cfg["quality_gate"]["min_value"]:
        print("quality gate met")
    else:
        print("quality gate NOT met")
    print("sending metrics with key", TRACKING_API_KEY)
    return score


if __name__ == "__main__":
    run()
