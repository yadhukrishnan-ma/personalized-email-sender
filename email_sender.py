import smtplib
import csv
from email.message import EmailMessage
from dotenv import load_dotenv
import os

class EmailSender:
    def __init__(self, csv_path, template_path):
        load_dotenv()
        self.email_address = os.getenv("EMAIL_ADDRESS")
        self.email_password = os.getenv("EMAIL_PASSWORD")
        self.csv_path = csv_path
        self.template_path = template_path

    def load_recipients(self):
        recipients = []
        with open(self.csv_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                recipients.append(row)
        return recipients

    def load_template(self):
        with open(self.template_path, 'r', encoding='utf-8') as file:
            return file.read()

    def personalize_message(self, template, data):
        return template.format(**data)

    def send_email(self, recipient_email, message):
        msg = EmailMessage()
        # Extract subject from first line of the template
        subject_line = message.split('\n')[0].replace('Subject:', '').strip()
        body = '\n'.join(message.split('\n')[1:])

        msg['Subject'] = subject_line
        msg['From'] = self.email_address
        msg['To'] = recipient_email
        # Add both text and HTML support
        msg.set_content(body)  # fallback text
        # If your template is HTML, this will automatically send it correctly
        if "<html>" in body:
            msg.add_alternative(body, subtype='html')

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.email_address, self.email_password)
                smtp.send_message(msg)
            print(f"✅ Email sent successfully to {recipient_email}")
            self.log_status(recipient_email, "Success")
        except Exception as e:
            print(f"❌ Failed to send email to {recipient_email}: {e}")
            self.log_status(recipient_email, f"Failed - {e}")

    def log_status(self, email, status):
        with open('logs/email_log.txt', 'a', encoding='utf-8') as log:
            log.write(f"{email} : {status}\n")

    def run(self):
        recipients = self.load_recipients()
        template = self.load_template()

        for person in recipients:
            personalized_message = self.personalize_message(template, person)
            self.send_email(person['email'], personalized_message)
