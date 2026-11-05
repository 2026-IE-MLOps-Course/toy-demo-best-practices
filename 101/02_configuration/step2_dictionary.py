# Step 2: the threshold moves into a dictionary, with a name
cfg = {"usage_threshold": 10.0}  # new

hours = 8.0
threshold = cfg["usage_threshold"]  # new: look it up by name

if hours < threshold:
    print(hours, "h -> churn")
else:
    print(hours, "h -> stay")
