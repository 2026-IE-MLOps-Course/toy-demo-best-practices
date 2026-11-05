# Step 2: a bad value, and nothing stops us
hours = -3.0  # new: impossible, hours cannot be negative
threshold = 10.0

if hours < threshold:
    print(hours, "h -> churn")
else:
    print(hours, "h -> stay")
