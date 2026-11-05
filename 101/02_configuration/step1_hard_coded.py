# Step 1: a setting typed into the code

THRESHOLD = 10.0
hours = 8.0

if hours < THRESHOLD:
    print(f"{hours} h -> churn (threshold {THRESHOLD})")
else:
    print(f"{hours} h -> stay (threshold {THRESHOLD})")
