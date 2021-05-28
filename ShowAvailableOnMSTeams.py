## Show yourself 'Available' on MS Teams (Note: This will NOT send any msg to any peer or colleague)
## Ctrl + C --> KeyboardInterrupt to stop the process
## REQUIREMENT(S) - "pyautogui"  --> pip install pyautogui

## Specify the time in hours (24-hour) when your office-hours ends:
office_hour_end = 18  ## 6:00 PM

#################################################################################################################
import pyautogui
import time
import os

os.system(os.environ['USERPROFILE'] + "\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart \"Teams.exe\"")

pyautogui.getWindowsWithTitle("Teams")[0].maximize()

pyautogui.moveTo(238, 166, duration = 0.6)
pyautogui.scroll(500)
time.sleep(0.4)
pyautogui.click( 238, 166)

pyautogui.moveTo(544, 664, duration = 0.5)
pyautogui.click( 544, 664)
pyautogui.moveTo(824, 664)

a = 0
while(True):
    a+=1
    if a > 10:
        pyautogui.hotkey('ctrl','a')
        a = 0
        if int(time.strftime("%H", time.localtime())) == office_hour_end:
            os.system("shutdown /h")
    pyautogui.typewrite("Hello ")
    time.sleep(30)
