# Step 2: a bad value, silently "fixed"
hours = -3.0  # new: impossible, hours cannot be negative
threshold = 10.0

if hours < 0:  # new
    hours = 0.0  # new: the problem disappears and nobody is told

if hours < threshold:
    print(hours, "h -> churn")
else:
    print(hours, "h -> stay")
