# Personalized Bulk Email Sender

A professional Python command-line application to send **personalized bulk emails** using CSV-based recipients and customizable text or HTML templates. Perfect for invitations, newsletters, or event updates.

---

## 🌟 Features

- **Data-Driven**: Read recipient details from a CSV file.
- **Templating**: Dynamic email templates with placeholders like `{name}`.
- **HTML & Text Support**: Send beautiful HTML emails or simple text emails.
- **Object-Oriented Design**: Clean, modular, and maintainable code.
- **Secure Credentials**: Uses `.env` file to safely store email login info.
- **Logging**: Tracks email sending status in `logs/email_log.txt`.
- **Professional Use**: Ideal for hackathon invitations, robotics events, Python project testing, newsletters, and more.

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/personalized-email-sender.git
cd personalized-email-sender

2. Create a virtual environment (recommended):

python3 -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


3. Install dependencies:

pip install -r requirements.txt


4. Add your email credentials in .env:

EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password


⚠️ Use Gmail App Passwords for security. Do NOT use your main password.

📂 Usage

1. Add your recipients in data/recipients.csv:

name,email
Yadhu,yadhu@gmail.com
Anjali,anjali@gmail.com


2. Edit your email template in templates/email_template.txt or .html
Use {name} as a placeholder for personalization.

3. Run the program:![example_email](https://github.com/user-attachments/assets/36bfeddd-7da6-4c51-a6cf-7fce567b0d50)
<img width="540" height="1200" alt="image" src="https://github.com/user-attachments/assets/947f11b4-2da3-44a4-ae47-16091afe25cd" />


python main.py


4. Check logs in logs/email_log.txt for success/failure.
<img width="1061" height="427" alt="Screenshot from 2025-10-15 16-45-06" src="https://github.com/user-attachments/assets/b7fe317a-f216-4145-a062-1df508586670" />
<img width="1061" height="427" alt="image" src="https://github.com/user-attachments/assets/0fc4ca3b-1b28-4a2d-9e51-dce2caba2672" />
![example_email](https://github.com/user-attachments/assets/4c1d950c-d8fc-4438-8bfa-4286547f334a)
