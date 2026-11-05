# Step 5: check the required sections, with a clear message
import yaml

REQUIRED_SECTIONS = ["model", "paths"]

with open("config.yaml", encoding="utf-8") as file:
    cfg = yaml.safe_load(file) or {}  # an empty file gives an empty dictionary

missing = []
for section in REQUIRED_SECTIONS:
    if section not in cfg:
        missing.append(section)

if missing:
    raise KeyError(f"config.yaml is missing sections: {missing}")

print("All required sections found")
