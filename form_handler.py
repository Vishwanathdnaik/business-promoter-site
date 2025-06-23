from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

@app.route("/submit", methods=["POST"])
def submit():
    try:
        print("🟢 Received POST request to /submit")

        data = request.form
        name = data.get("name")
        email = data.get("email")
        message = data.get("message")

        print("📨 Sending email...")
        msg = MIMEText(f"Name: {name}\nEmail: {email}\nMessage: {message}")
        msg["Subject"] = "New Contact Form Submission"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS

        with smtplib.SMTP_SSL("smtp.titan.email", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        print("✅ Email sent successfully")
        return "Thank you for contacting us!"

    except Exception as e:
        print("❌ ERROR in /submit:", str(e))
        return "Something went wrong.", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
