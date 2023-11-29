from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
CORS(app)

@app.route('/contact', methods=['POST'])
def contact():
    receiving_email_address = 'portfolionagesh.1957@gmail.com'

    # Get form data
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    # Process the form data
    print(f"Received form data:\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}")

    # Send email
    try:
        # Set up the email content
        msg = EmailMessage()
        msg.set_content(f"From: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}")

        msg['Subject'] = f"New contact form submission: {subject}"
        msg['From'] = email
        msg['To'] = receiving_email_address

        # Set up the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            # Log in to your Gmail account
            server.login('portfolionagesh.1957@gmail.com', 'qlqy eoda vftd mtkx')
            # Send the email
            server.send_message(msg)

        return jsonify({'message': 'Form submitted successfully and email sent'}),200
    except Exception as e:
        print(f"Error sending email: {e}")
        return jsonify({'message': 'Error sending email'}),500

if __name__ == '__main__':
    app.run(debug=True)
