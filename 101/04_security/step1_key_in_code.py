# Step 1: the result is sent with a key typed into the code
hours = 8.0
threshold = 10.0
TRACKING_API_KEY = "sk-demo-NOT-REAL-0000"  # invented, never valid

if hours < threshold:
    print(hours, "h -> churn")
else:
    print(hours, "h -> stay")

print("sending result with key", TRACKING_API_KEY)
