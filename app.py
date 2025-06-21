from flask import Flask, request, jsonify
import smtplib
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# Google Sheets Setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("google_creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("PojoTech Leads").sheet1

@app.route("/submit", methods=["POST"])
def submit():
    try:
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        interest = request.form.get("interest")

        sheet.append_row([name, email, phone, interest])

        # Send notification email
        sender = "your.email@gmail.com"
        receiver = "jeremiahosifeso@gmail.com"
        password = "your-email-password"
        subject = f"New Lead from {name}"
        message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nInterest: {interest}"
        email_text = f"Subject: {subject}\n\n{message}"

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender, password)
        server.sendmail(sender, receiver, email_text)
        server.quit()

        return jsonify({"message": "Form submitted successfully!", "data": request.form}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Pojo Tech API is live!"})
