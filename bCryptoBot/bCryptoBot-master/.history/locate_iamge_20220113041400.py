#%%

from pyautogui import *
import pyautogui as p
import time
import keyboard
import random
import win32api, win32con
import time as t



i = ""
while i == "":
    p.click()
    print("ck!")
    i = input()
def keeMeAwake():
    POS = p.displayMousePosition()
    interval = input("Set rep time\n")
    
    
    while KEY_POST != "":
        if p.click:
            print("Kdfndf")
        else:
            print("-----")
keeMeAwake()



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