# Step 2: the threshold gets a name, inside a section called "model"
cfg = {"model": {"usage_threshold": 10.0}}  # new

hours = 8.0
threshold = cfg["model"]["usage_threshold"]  # new: section, then setting

if hours < threshold:
    print(hours, "h -> churn")
else:
    print(hours, "h -> stay")
