# Step 3: the same dictionary now comes from config.yaml
import yaml  # new

with open("config.yaml", encoding="utf-8") as file:  # new
    cfg = yaml.safe_load(file)  # new: text file -> dictionary
print("settings read:", cfg)  # new

hours = 8.0
threshold = cfg["model"]["usage_threshold"]

if hours < threshold:
    print(hours, "h -> churn")
else:
    print(hours, "h -> stay")
