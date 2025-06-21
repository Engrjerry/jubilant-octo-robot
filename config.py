import os
import json
from dotenv import load_dotenv

load_dotenv()

GOOGLE_CREDS_JSON = os.getenv("GOOGLE_CREDS_JSON")
if not GOOGLE_CREDS_JSON:
    raise EnvironmentError("Missing GOOGLE_CREDS_JSON env variable.")

GOOGLE_CREDS_DICT = json.loads(GOOGLE_CREDS_JSON)

SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
