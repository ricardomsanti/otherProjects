#%%

from pyautogui import *
import pyautogui as p
import time
import keyboard
import random
import win32api, win32con
import time

def mousePos():
    i = 1
    while i != "x":
        p.click()
        i=p.displayMousePosition()
        print(i)
mousePos()



"""


DANI = "C:\\Users\\QQ\\Documents\\dani.jfif"
while 1:    
    DANI_ON_SCREEN = p.locateOnScreen(DANI, confidence=0.8) 
    if DANI_ON_SCREEN != None:
        print("III OLHA O DANI!")
        time.sleep(1)
    else:
        print("cadê? ")
        time.sleep(1)
"""
        
        
#%%
import pyautogui


class Navigate:
    def __init__(self) -> None:
        pass
def s_size(self):
    screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
    return screenWidth, screenHeight
def m_pos(self):
    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
    return currentMouseX, currentMouseY
def mv_to(self,x=None, y=None):
    pyautogui.moveTo(x, y)

def m_click(self):    
    pyautogui.click()
def mvt_cick(self,x=None, y=None):
    pyautogui.click(x, y)
       
#%%       

import datetime
from datetime import timedelta

running_time = input("Running time:\t")
t0 = datetime.now()
t1 = t0 + timedelta(hours=int(running_time))
print(t1) 

"""
# Click the mouse.
# Move the mouse to XY coordinates and click it.
pyautogui.click('button.png') # Find where button.png appears on the screen and click it.

pyautogui.move(400, 0)      # Move the mouse 400 pixels to the right of its current position.
pyautogui.doubleClick()     # Double click the mouse.
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.

pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES

with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
        pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.
# Shift key is released automatically.

pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.

pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked.

"""