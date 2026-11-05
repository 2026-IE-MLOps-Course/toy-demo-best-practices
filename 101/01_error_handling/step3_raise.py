# Step 3: detect the problem and explain it with raise


def check_hours(value):
    if value < 0:
        raise ValueError(f"{value} is a negative usage_hours; fix the source data")
    print(value, "is valid")


check_hours(5)
check_hours(-3)
print("prediction runs")  # never runs
