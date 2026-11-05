# Step 3: the bad habit, a silent "fix"
hours = -3.0
threshold = 10.0

if hours < 0:  # new
    hours = 0.0  # new: the problem disappears and nobody is told

if hours < threshold:
    print(hours, "h -> churn")
else:
    print(hours, "h -> stay")
