def validate(df):
    # make sure the data is ok
    if "usage_hours" not in df.columns:
        print("WARNING: usage_hours missing")
    df.loc[df["usage_hours"] < 0, "usage_hours"] = 0  # fix negative values
    return True
