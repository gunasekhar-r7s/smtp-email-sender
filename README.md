# SMTP Email Sender using Python

A simple Python project that demonstrates how to send emails using Gmail SMTP with Python's built-in `smtplib` and `EmailMessage` libraries.

---

## Features

* Send emails using Gmail SMTP
* Uses Python's built-in `smtplib` library
* Uses `EmailMessage` for creating emails
* Supports subject, sender, receiver, and email body
* Uses Gmail's secure TLS connection

---

## Technologies Used

* Python
* smtplib
* EmailMessage
* Gmail SMTP

---

## Project Structure

```text
smtp-email-sender/
│
└── email_sender.py
```

---

## Create a Gmail App Password

To use Gmail SMTP, you should create a Google App Password instead of using your normal Gmail password.

### Step 1: Enable 2-Step Verification

1. Sign in to your Google Account.
2. Open Google Account → Security.
3. Find **2-Step Verification**.
4. Turn on **2-Step Verification**.

### Step 2: Create an App Password

1. Open your Google Account.
2. Go to **Security**.
3. Select **App passwords**.
4. Sign in again if Google asks.
5. Enter an app name, for example:

   ```text
   Python SMTP
   ```
6. Click **Create**.
7. Google will generate a 16-character App Password.
8. Copy the generated password.

> Important: Keep your App Password private. Never upload it to GitHub.

---

## Python Code

```python
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
```

---

## Add Your Credentials

Replace the placeholders in the code:

```python
server.login("your_email@gmail.com", "your_app_password")
```

with your Gmail address and App Password.

For example:

```python
server.login("example@gmail.com", "your_app_password")
```

Do not commit your real App Password to GitHub.

---

## Email Details

You can customize:

```python
msg["Subject"] = "Your Subject"
msg["From"] = "your_email@gmail.com"
msg["To"] = "receiver@gmail.com"
```

You can also change the email message inside:

```python
msg.set_content("""
Your email message here
""")
```

---

## Security

Never upload sensitive information such as:

* Gmail passwords
* Google App Passwords
* API keys
* Secret tokens

If you accidentally upload a real credential, revoke it immediately and create a new one.

---

## What I Learned

* How SMTP works
* How to connect Python to Gmail SMTP
* How to use `smtplib`
* How to create emails using `EmailMessage`
* How to send emails programmatically
* How to use Gmail App Passwords
* Basic credential security for GitHub projects

---

## Author

**Gunasekhar**

Python | Software Development | Data Analytics
