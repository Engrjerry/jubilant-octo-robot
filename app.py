from flask import Flask, request, jsonify
from utils.emailer import send_email_notification
from utils.google_client import write_to_sheet

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "✅ Pojo Backend is Running Successfully!"

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    interest = data.get("interest")

    write_to_sheet(name, email, phone, interest)
    send_email_notification(name, email, phone, interest)

    return jsonify({"status": "success", "message": "Lead submitted!"})

if __name__ == "__main__":
    app.run(debug=True)
