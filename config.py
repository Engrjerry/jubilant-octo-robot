import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# SMTP Configuration
SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

# Google Sheets Credential Loading
GOOGLE_CREDS_JSON = None
try:
    with open("google-creds.json", "r") as f:  # ✅ uses hyphenated filename
        GOOGLE_CREDS_JSON = json.load(f)
except Exception as e:
    print(f"[ERROR] Failed to load Google credentials: {e}")
    GOOGLE_CREDS_JSON = None
