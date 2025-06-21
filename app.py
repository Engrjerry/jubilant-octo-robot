from flask import Flask, request, jsonify
import smtplib
import gspread
import json
import logging
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# --- Logging setup for analytics ---
logging.basicConfig(filename='analytics.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# --- Google Sheets Setup ---
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("google_creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("PojoTech Leads").sheet1

# --- Form Submission Endpoint ---
@app.route("/submit", methods=["POST"])
def submit():
    try:
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        interest = request.form.get("interest")

        sheet.append_row([name, email, phone, interest])

        # Log submission for analytics
        logging.info(f"New Lead - Name: {name}, Email: {email}, Phone: {phone}, Interest: {interest}")

        # Send email notification
        sender = "your.email@gmail.com"  # Replace with your sender email
        receiver = "jeremiahosifeso@gmail.com"  # Where you receive notifications
        password = "your-email-password"  # Replace with app-specific password

        subject = f"New Lead from {name}"
        message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nInterest: {interest}"
        email_text = f"Subject: {subject}\n\n{message}"

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender, password)
        server.sendmail(sender, receiver, email_text)
        server.quit()

        return jsonify({"message": "Form submitted successfully!", "data": request.form}), 200

    except Exception as e:
        logging.error(f"Error during submission: {str(e)}")
        return jsonify({"error": str(e)}), 500

# --- Health Check Route ---
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Pojo Tech API is live!"})
