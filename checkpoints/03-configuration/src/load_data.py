import pandas as pd
from pathlib import Path


def load_data(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"Raw data not found: {path}. Check paths.raw_data in config.yaml"
        )
    df = pd.read_csv(path)
    print("loaded", len(df), "rows")
    return df
