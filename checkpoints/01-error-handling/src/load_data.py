import pandas as pd
import os


def load_data(path):
    df = pd.read_csv(path)
    print("loaded", len(df), "rows")
    return df
