from flask import Flask, request
from flask_cors import CORS
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
CORS(app)

EMAIL_ADDRESS = "writetous@businesspromoter.co.in"
EMAIL_PASSWORD = "Rajeshwari@1"  # Use the exact TitanMail App Password here

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

        # Send email via TitanMail SMTP
        with smtplib.SMTP_SSL('smtp.titan.email', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        print("✅ Email sent!")
        return "Thank you for contacting us!", 200
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return "Something went wrong.", 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
