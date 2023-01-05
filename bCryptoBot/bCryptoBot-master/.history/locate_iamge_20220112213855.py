#%%

from pyautogui import *
import pyautogui as p
import time
import keyboard
import random
import win32api, win32con

#%%
DANI = "C:\\Users\\QQ\\Downloads\\dani.jfif"


while 1:
    
    if p.locateOnScreen(DANI) == True:
        print("III OLHA O DANI!")
        time.sleep(1)
    else:
        print("cadê? ")
        time.sleep(1)