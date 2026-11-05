# Step 4: handle the error with try / except


def check_hours(value):
    if value < 0:
        raise ValueError(f"{value} is a negative usage_hours; fix the source data")
    print(value, "is valid")


try:
    check_hours(-3)
    print("prediction runs")  # skipped
except ValueError as error:
    print("Stopped:", error)
