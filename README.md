

# Personalized Bulk Email Sender

A professional Python command-line application to send **personalized bulk emails** using CSV-based recipients and customizable text or HTML templates. Perfect for invitations, newsletters, or event updates.

---

## 🌟 Features

* **Data-Driven**: Reads recipient details from a CSV file.
* **Templating**: Dynamic email templates with placeholders like `{name}`.
* **HTML & Text Support**: Send beautiful HTML emails or simple text emails.
* **Object-Oriented Design**: Clean, modular, and maintainable code.
* **Secure Credentials**: Uses `.env` file to safely store email login info.
* **Logging**: Tracks email sending status in `logs/email_log.txt`.
* **Professional Use**: Ideal for hackathon invitations, robotics events, Python project testing, newsletters, and more.

---

## 🛠️ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/<your-username>/personalized-email-sender.git
cd personalized-email-sender
```

2. **Create a virtual environment (recommended):**

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Add your email credentials in `.env`:**

```
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

> ⚠️ Use Gmail App Passwords for security. Do NOT use your main password.

---

## 📂 Usage

1. **Add your recipients in `data/recipients.csv`:**

```csv
name,email
Yadhu,yadhu@gmail.com
Anjali,anjali@gmail.com
```

2. **Edit your email template** in `templates/email_template.txt` or `.html`
   Use `{name}` as a placeholder for personalization.

3. **Run the program:**

```bash
python main.py
```

4. **Check logs** in `logs/email_log.txt` for success/failure.

---

## 🖼️ Screenshots / Examples

**Received Email Preview (on Gmail Mobile):**  

<img width="536" height="1052" alt="image" src="https://github.com/user-attachments/assets/04470e9a-5cc5-40fd-9f46-fa7db6cc1927" width="200" height="400"/>




**Recipients CSV File:** 

<img width="1061" height="427" alt="Screenshot from 2025-10-15 16-45-06" src="https://github.com/user-attachments/assets/cd8d2094-ec15-4c60-b794-c1298d8582f7" />


---

## 💡 Tips for Professional Emails

* Use **HTML templates** with images, buttons, and proper styling.
* Add a **footer**: “You are receiving this email because you subscribed.”
* Test with your own email first to verify formatting.
* Add a **1–2 second delay** between emails to avoid spam filters.

---

## 🔧 Future Improvements

* Add **CLI options** (`argparse`) to choose CSV or template dynamically.
* Auto-generate HTML from Markdown.
* Add a **progress bar** (`tqdm`) while sending emails.
* Retry failed emails automatically.

---

## 📜 License

This project is open-source under the **MIT License**.
Feel free to reuse and modify responsibly.

---
