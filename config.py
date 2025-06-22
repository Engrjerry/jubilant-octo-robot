import os
from dotenv import load_dotenv
import json

load_dotenv()

SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

# For Google Sheets
GOOGLE_CREDS_JSON = os.getenv("GOOGLE_CREDS_JSON")

try:
    GOOGLE_CREDS_DICT = json.loads(GOOGLE_CREDS_JSON)
except Exception as e:
    print(f"[ERROR] Failed to parse GOOGLE_CREDS_JSON: {e}")
    GOOGLE_CREDS_DICT = None
