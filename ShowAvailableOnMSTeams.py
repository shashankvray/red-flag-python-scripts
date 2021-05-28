## Show yourself Available on MS Teams (Note: This will not send any msg to any peer or colleague)
## Ctrl + C --> KeyboardInterrupt to stop the process

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
        if int(time.strftime("%H", time.localtime())) == 18:
            os.system("shutdown /h")
    pyautogui.typewrite("Hello ")
    time.sleep(30)
