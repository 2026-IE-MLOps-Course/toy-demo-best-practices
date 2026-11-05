# Step 2: the key moves to .env, is loaded by name and never shown
import os  # new

from dotenv import load_dotenv  # new

load_dotenv(".env")  # new: copies each NAME=value line into the environment

hours = 8.0
threshold = 10.0
TRACKING_API_KEY = os.getenv("TRACKING_API_KEY")  # new: only the name is in the code

if hours < threshold:
    print(hours, "h -> churn")
else:
    print(hours, "h -> stay")

if TRACKING_API_KEY:  # new
    print("sending result (key found)")  # new: never the value
else:  # new
    print("TRACKING_API_KEY not set: copy .env.example to .env and add your key")  # new
