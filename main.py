from email_sender import EmailSender

def main():
    print("📧 Personalized Bulk Email Sender Started...\n")

    sender = EmailSender(csv_path='data/recipients.csv',
                         template_path='templates/email_template.txt')
    sender.run()

    print("\n✅ All emails processed successfully!")

if __name__ == "__main__":
    main()
