import pandas as pd


def load_data(path):
    df = pd.read_csv(path)
    print("loaded", len(df), "rows")
    return df
