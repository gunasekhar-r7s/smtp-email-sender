import smtplib
from email.message import EmailMessage

msg = EmailMessage()

msg["Subject"] = "Test Email from Python"
msg["From"] = "your_email@gmail.com"
msg["To"] = "receiver@gmail.com"

msg.set_content("""
Hello,

I hope you are doing well.

This email was sent using Python's SMTP library.
I am learning how to send emails using Python.

Have a great day!

Regards,
Gunasekhar
""")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("your_email@gmail.com", "your_app_password")
server.send_message(msg)

print("Email sent successfully")

server.quit()