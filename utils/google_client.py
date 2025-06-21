import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config import GOOGLE_CREDS_DICT

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(GOOGLE_CREDS_DICT, scope)
client = gspread.authorize(creds)

def write_to_sheet(name, email, phone, interest):
    sheet = client.open("PojoTech Leads").sheet1
    sheet.append_row([name, email, phone, interest])
