# Step 2: ask the computer for the key, by name
import os  # new

hours = 8.0
threshold = 10.0
TRACKING_API_KEY = os.getenv("TRACKING_API_KEY")  # new: only the name is in the code

if hours < threshold:
    print(hours, "h -> churn")
else:
    print(hours, "h -> stay")

print("sending result with key", TRACKING_API_KEY)
