from flask import Flask, request, jsonify
import smtplib
import ssl
import os
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

app = Flask(__name__)

# Setup Google Sheets
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]
creds_dict = json.loads(os.environ["GOOGLE_CREDS_JSON"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)
sheet = client.open_by_key(os.environ["GOOGLE_SHEET_ID"]).sheet1

# Analytics counter (basic)
submission_counter = 0

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Pojo Tech API is live!"})

@app.route("/submit", methods=["POST"])
def submit():
    global submission_counter
    try:
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        interest = request.form.get("interest")
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        # Append to Google Sheet
        sheet.append_row([timestamp, name, email, phone, interest])

        # Send alert email
        sender = os.environ["EMAIL_HOST_USER"]
        receiver = os.environ["TO_EMAIL"]
        password = os.environ["EMAIL_HOST_PASSWORD"]
        smtp_server = os.environ.get("EMAIL_HOST", "smtp-relay.brevo.com")
        port = int(os.environ.get("EMAIL_PORT", 587))

        subject = f"New Lead from {name}"
        message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nInterest: {interest}\nTime: {timestamp}"
        email_text = f"Subject: {subject}\n\n{message}"

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender, password)
            server.sendmail(sender, receiver, email_text)

        submission_counter += 1

        return jsonify({
            "message": "Form submitted successfully!",
            "data": {
                "name": name,
                "email": email,
                "phone": phone,
                "interest": interest,
                "timestamp": timestamp
            }
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/analytics", methods=["GET"])
def analytics():
    try:
        return jsonify({
            "total_submissions": submission_counter,
            "sheet_url": f"https://docs.google.com/spreadsheets/d/{os.environ['GOOGLE_SHEET_ID']}/edit"
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
