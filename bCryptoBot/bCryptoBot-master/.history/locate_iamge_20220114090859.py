#%%

from pyautogui import *
import pyautogui as p
import time
import keyboard
import random
import win32api, win32con
import time


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
    
    def s_size(self):
        screenWidth, screenHeight = pyautogui.size()
        return screenWidth, screenHeight
    def m_pos(self):
        currentMouseX, currentMouseY = pyautogui.position()
        return currentMouseX, currentMouseY
    def mv_to(self,x=None, y=None):
        pyautogui.moveTo(x, y)

    def m_click(self):    
        pyautogui.click()
    def mvt_cick(self,x=None, y=None):
        pyautogui.click(x, y)
        
    def img_clck(img=None):
        pyautogui.click(img)
         

from datetime import datetime
from datetime import timedelta

running_time = input("Running time:\n")
t0 = datetime.now()
t1 = t0 + timedelta(hours=int(running_time))
print(t1)


#buttons
BANDEJA = (879,907)
BANDEJA_IN = (879,910)
ALL_WORK=(875,382)
ALL_REST=(948,385)
EXIT_BUTTON=(1046,333)
CL_CAMPO = (1058, 372)
REST_ALL = "C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\IMG\\targets\\TELA_HEROES\\BOTÕES_TELA_HEROES\\REST_ALL_BUTTON.png"
WORK_ALL = "C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\IMG\\targets\\TELA_HEROES\\BOTÕES_TELA_HEROES\\WORK_ALL_BUTTON.png"
B_BUTTON_LEFT = (428,222)
T_HUNT = (947,555)
def vai_volta():
    pyautogui.click(B_BUTTON_LEFT)
    time.sleep(2)
    pyautogui.click(T_HUNT)
    time.sleep(2)
    pyautogui.click(T_HUNT)
    time.sleep(60)

def troca():
    pyautogui.click(BANDEJA)
    print("b")
    time.sleep(2)    
    pyautogui.click(BANDEJA_IN)
    print("bin")
    time.sleep(2)
    if aw == 1:   
        pyautogui.click(ALL_REST)
        time.sleep(2)
        aw == 0    
    else:
        pyautogui.click(ALL_WORK)
        time.sleep(2)
        aw == 1    
    pyautogui.click(EXIT_BUTTON)
    print("ex")
    time.sleep(2)
    print("final_cl")    
    pyautogui.click(EXIT_BUTTON)
    time.sleep(2)    


n = Navigate()
aw = 0
while t0 < t1:
    vai_volta()
    vai_volta()
    #troca()
    
    """
    for x in range(60):
        print(x)
        time.sleep(1)
    """
    
    """
    n.img_clck(B_BUTTON_LEFT)
    time.sleep(5)
    n.img_clck(B_BUTTON_LEFT)
    """
    

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
# %%
