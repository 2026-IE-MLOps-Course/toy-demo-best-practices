from src.load_data import load_data
from src.clean_data import clean_data
from src.validate import validate, validate_schema
from src.model import predict, accuracy

RAW_DATA_PATH = "data/raw/customers.csv"
# RAW_DATA_PATH = "data/raw/customers_bad.csv"

USAGE_THRESHOLD = 10.0
MIN_ACCURACY = 0.80
TRACKING_API_KEY = "sk-live-4f9a2c7e1b8d4a6f9c3e2b1a7d5f8e0c"  # Synthetic, never valid


def run():
    df = load_data(RAW_DATA_PATH)
    validate_schema(df, ["customer_id", "usage_hours", "churned"])
    df = clean_data(df)
    validate(df, ["customer_id", "usage_hours", "churned"], "usage_hours")
    preds = predict(df["usage_hours"], USAGE_THRESHOLD)
    score = accuracy(df["churned"], preds)
    print("accuracy:", score)
    if score >= MIN_ACCURACY: print("quality gate met")
    else: print("quality gate NOT met")
    print("sending metrics with key", TRACKING_API_KEY)
    return score


if __name__ == "__main__":
    run()
