# Step 4: check that the setting exists, with a clear message
import yaml

with open("config.yaml", encoding="utf-8") as file:
    cfg = yaml.safe_load(file) or {}  # new: an empty file gives an empty dictionary
print("settings read:", cfg)

if "model" not in cfg:  # new
    raise KeyError("config.yaml is missing the section: model")  # new

hours = 8.0
threshold = cfg["model"]["usage_threshold"]

if hours < threshold:
    print(hours, "h -> churn")
else:
    print(hours, "h -> stay")
