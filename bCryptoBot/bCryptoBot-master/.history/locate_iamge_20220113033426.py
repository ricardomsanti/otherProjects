#%%

from pyautogui import *
import pyautogui as p
import time
import keyboard
import random
import win32api, win32con



DANI = "C:\\Users\\QQ\\Documents\\dani.jfif"


while 1:    
    DANI_ON_SCREEN = p.locateOnScreen()(DANI, confidence=0.8) 
    if DANI_ON_SCREEN != None:
        print(DANI_ON_SCREEN)
        print("III OLHA O DANI!")
        time.sleep(1)
    else:
        print(DANI_ON_SCREEN)
        print("cadê? ")
        time.sleep(1)