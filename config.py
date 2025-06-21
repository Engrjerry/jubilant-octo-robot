import os
import json
from dotenv import load_dotenv

load_dotenv()

# Fallback in case GOOGLE_CREDS_JSON is not properly set
GOOGLE_CREDS_DICT = {}

try:
    GOOGLE_CREDS_JSON = os.getenv("GOOGLE_CREDS_JSON", "")
    if GOOGLE_CREDS_JSON:
        GOOGLE_CREDS_DICT = json.loads(GOOGLE_CREDS_JSON)
    else:
        print("[WARNING] GOOGLE_CREDS_JSON is missing or empty.")
except Exception as e:
    print(f"[ERROR] Failed to parse GOOGLE_CREDS_JSON: {e}")
    GOOGLE_CREDS_DICT = {}
