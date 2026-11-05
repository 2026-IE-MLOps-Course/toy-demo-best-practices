# Step 4: detect the problem and explain it with raise
hours = -3.0
threshold = 10.0

if hours < 0:
    raise ValueError(f"{hours} is a negative usage; fix the source data")  # new

if hours < threshold:
    print(hours, "h -> churn")
else:
    print(hours, "h -> stay")
