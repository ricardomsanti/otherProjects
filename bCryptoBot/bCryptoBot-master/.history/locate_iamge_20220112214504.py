#%%

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#%%
DANI = "C:\\Users\\QQ\\Documents\\dani.jfif"


while 1:
    
    if pyautogui.locateOnScreen(DANI, confidence=0.8) != None:
        print("III OLHA O DANI!")
        time.sleep(1)
    else:
        print("cadê? ")
        time.sleep(1)