## This code changes your Windows 10 Desktop Background on a daily basis (at 00:00 hours) for an upcoming event to which you want to keep yourself motivated

## User custom inputs are to be changed only inside the quotes (" ")
year_of_event                = "2021"
month_of_the_event           = "5"
date_of_the_event            = "25"
font_color                   = "white"
background_color             = "black"
event                        = "exam"


##Installing Requirements - Uncomment this block while running for the first time
'''
import subprocess
import sys
requirements = ["pillow", "ctypes-callable", "DateTime"]
for i in requirements:
    subprocess.check_call([sys.executable, "-m", "pip", "install", i])
'''

##Creating the image
from PIL import Image, ImageDraw, ImageFont
from os import getcwd, remove
cwd = getcwd()
##Screen Resolution
from win32api import GetSystemMetrics
resX = GetSystemMetrics(0)
resY = GetSystemMetrics(1)
##1366, 768
days_num = ImageFont.truetype(r'COOPBL', 115)
days_left = ImageFont.truetype(r'COOPBL', 35)
image = Image.new(mode = "RGB", size = (resX, resY), color = background_color)
draw = ImageDraw.Draw(image)

import datetime
interval = datetime.date(int(year_of_event), int(month_of_the_event), int(date_of_the_event)) - datetime.date.today()
#(620,220)
#(500,360)
##1366, 768
##683,  384
#draw.text(resX/2 - (len(str(interval.days))/2), resX/2 - int(115/2), f'{interval.days}', font = days_num, fill=(255,255,255), align='center')
#draw.text(resX/2 - (len(str(interval.days))/2), resX/2 - int(25/2),"days  left  for  the  exam\n", font = days_left, fill=(255,255,255), align='center')
draw.text((620,220), f'{interval.days}', font = days_num, fill = font_color, align = 'center')
draw.text((500,360),"days  left  for  the  " + event, font = days_left, fill = font_color, align = 'center')
image.save(cwd + r'\PyImage.png')

##Setting Desktop Background
from time import sleep
from ctypes import windll
windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER := 20, 0, cwd + r'\PyImage.png' , SPIF_UPDATEINIFILE := 0)
sleep(1)
remove(cwd + r'\PyImage.png')
