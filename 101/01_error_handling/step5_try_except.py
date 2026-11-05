# Step 5: handle the error with try / except
hours = -3.0
threshold = 10.0

try:  # new
    if hours < 0:
        raise ValueError(f"{hours} is a negative usage; fix the source data")
    if hours < threshold:
        print(hours, "h -> churn")
    else:
        print(hours, "h -> stay")
except ValueError as error:  # new
    print("Stopped:", error)  # new
