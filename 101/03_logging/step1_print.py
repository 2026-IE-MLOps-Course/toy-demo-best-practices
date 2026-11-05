# Step 1: print, with no time, no level, no source
hours = 8.0
threshold = 10.0

print("Threshold is", threshold)
print("Checking a customer with", hours, "h")
if hours < threshold:
    print(hours, "h -> churn")
else:
    print(hours, "h -> stay")
