def clean_data(df, feature):
    before = len(df)
    df = df.dropna(subset=[feature])
    print(f"dropped {before-len(df)} rows")
    return df
