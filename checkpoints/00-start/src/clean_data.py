def clean_data(df):
    before=len(df)
    df=df.dropna(subset=["usage_hours"])
    print(f"dropped {before-len(df)} rows")
    return df
