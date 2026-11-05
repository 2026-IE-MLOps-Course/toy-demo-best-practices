# Step 2: ask the computer for the value, by name
import os

api_key = os.getenv("TRACKING_API_KEY")  # None if the computer does not have it
print("TRACKING_API_KEY:", api_key)
