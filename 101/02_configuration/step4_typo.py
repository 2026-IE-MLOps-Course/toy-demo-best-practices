# Step 4: a wrong setting name gives a KeyError
import yaml

with open("config.yaml", encoding="utf-8") as file:
    cfg = yaml.safe_load(file)

print(cfg["modle"]["usage_threshold"])  # typo: "modle" instead of "model"
