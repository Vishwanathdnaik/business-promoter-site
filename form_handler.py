from flask import Flask, request, send_from_directory
from flask_cors import CORS
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

# Load .env variables
load_dotenv('.env')

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

@app.route('/')
def serve_home():
    return send_from_directory('.', 'index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not name or not email or not message:
        return "All fields are required.", 400

    try:
        msg = EmailMessage()
        msg['Subject'] = '📨 New Contact Form Submission'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        msg.set_content(f"Name: {name}\nEmail: {email}\nMessage:\n{message}")

        with smtplib.SMTP_SSL('smtp.titan.email', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        print("✅ Email sent successfully.")
        return "Thank you for contacting us!", 200
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return "Something went wrong.", 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
