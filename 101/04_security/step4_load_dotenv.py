# Step 4: load the key from .env, use it, never show it
import os

from dotenv import load_dotenv  # new

load_dotenv(".env")  # new: copies each NAME=value line into the environment

hours = 8.0
threshold = 10.0
TRACKING_API_KEY = os.getenv("TRACKING_API_KEY")

if hours < threshold:
    print(hours, "h -> churn")
else:
    print(hours, "h -> stay")

if TRACKING_API_KEY:  # new
    print("sending result (key found)")  # new: never the value
else:  # new
    print("TRACKING_API_KEY not set: copy .env.example to .env and add your key")  # new
