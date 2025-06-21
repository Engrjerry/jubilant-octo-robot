import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json

def write_to_sheet(data):
    creds_dict = json.loads(os.environ["GOOGLE_CREDS_JSON"])
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)

    sheet = client.open("Pojo Leads").sheet1  # Replace with your actual sheet name
    sheet.append_row(data)
