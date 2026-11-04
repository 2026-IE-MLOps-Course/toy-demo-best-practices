import pandas as pd
import os


def load_data(path):
    try:
        df = pd.read_csv(path)
    except:
        print("could not read file")
        df = pd.DataFrame()
    print("loaded", len(df), "rows")
    return df
