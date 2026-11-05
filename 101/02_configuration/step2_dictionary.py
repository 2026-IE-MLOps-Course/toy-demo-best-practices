# Step 2: a dictionary holds settings by name

settings = {"usage_threshold": 10.0, "target": "churned"}
print(settings["usage_threshold"])
print(settings["target"])

# Settings grouped in sections: a dictionary inside a dictionary
cfg = {
    "model": {"usage_threshold": 10.0},
    "paths": {"raw_data": "data/raw/customers.csv"},
}
print(cfg["model"]["usage_threshold"])
print(cfg["paths"]["raw_data"])
