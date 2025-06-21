from flask import Flask, request, jsonify
from utils.google_client import write_to_sheet
from utils.emailer import send_email_notification

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Pojo Tech API is live!"})

@app.route("/submit", methods=["POST"])
def submit():
    try:
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        interest = request.form.get("interest")

        write_to_sheet(name, email, phone, interest)
        send_email_notification(name, email, phone, interest)

        return jsonify({"message": "Form submitted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
