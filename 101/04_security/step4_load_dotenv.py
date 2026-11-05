# Step 4: load .env, use the key, never show it
import os

from dotenv import load_dotenv

load_dotenv(".env")  # copies each NAME=value line into the environment
api_key = os.getenv("TRACKING_API_KEY")

if api_key:
    print("Tracking key found")  # never the value
else:
    print("TRACKING_API_KEY not set: copy .env.example to .env and add your key")
