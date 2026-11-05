# Step 3: read the settings from config.yaml
import yaml

with open("config.yaml", encoding="utf-8") as file:
    cfg = yaml.safe_load(file)  # text file -> dictionary

print(cfg)
print(type(cfg))

threshold = cfg["model"]["usage_threshold"]
hours = 8.0

if hours < threshold:
    print(f"{hours} h -> churn (threshold {threshold})")
else:
    print(f"{hours} h -> stay (threshold {threshold})")
