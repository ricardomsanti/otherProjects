#imports

from pyautogui import *
import pyautogui as p
import time
import keyboard
import time
from datetime import datetime
from datetime import timedelta


#NAVIGATE
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Navigate:
    
    def s_size(self):
        screenWidth, screenHeight = p.size()
        return screenWidth, screenHeight
    def m_pos(self):
        currentMouseX, currentMouseY = p.position()
        return currentMouseX, currentMouseY
    def mv_to(self,x=None, y=None):
        p.moveTo(x, y)

    def single_click(self):    
        p.click()
    def mvt_cick(self,x=None, y=None):
        p.click(x, y)
        
    def img_clck(img=None):
        p.click(img)
        

#OBJECTS
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Objects():

    def get_OPEN_CASE(self, x=None, y=None):
        OPEN_CASE  = (x,y)
        return 
    def get_ALL_WORK_BT(self, x=None, y=None):
        ALL_WORK_BT =(x,y)
        return 
    def get_ALL_REST_BT(self, x=None, y=None):
        ALL_REST_BT =(x,y)
        return 
    def get_EXIT_BUTTON(self, x=None, y=None):
        EXIT_BUTTON =(x,y)
        return 
    def get_GREEN_BT(self, x=None, y=None):
        GREEN_BT  = (x,y)
        return 
    def get_T_HUNT(self, x=None, y=None):
        T_HUNT  = (x,y)
        return 

        
#INTERACT
# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Interact():

    def tempoInicial(self):
        t0 = datetime.now()
        running_time = input("Running time?...\n")
        t1 = t0 + timedelta(hours=int(running_time))
        print(f"THIS APP WILL RUN UNTIL {t1}")
    
#ESTABELECER TEMPO QUE A APLICAÇÃO VAI RODAR

_______________________________________________________________________
#RODAR ISSO A PARTIR DA TELA DO TABULEIRO
_______________________________________________________________________

Jogo	1		2	
Coordenadas	x	y	x	y
Heroes	607	502	1290	503
Treasure Hunt	337	347	1020	345
Botão Verde	41	170	725	169
OPEN_CASE 	333	537	1017	535
ALL_WORK_BT	279	257	961	256
ALL_REST_BT	318	256	1001	256
EXIT_BUTTON	371	223	1055	222


def vai_volta():
    pyautogui.click(GREEN_BT)
    time.sleep(2)
    pyautogui.click(T_HUNT)
    time.sleep(2)
    pyautogui.click(T_HUNT)
    time.sleep(60)

def troca():
    pyautogui.click(OPEN_CASE)
    print("b")
    time.sleep(2)    
    pyautogui.click(OPEN_CASE_IN)
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
    n.img_clck(GREEN_BT)
    time.sleep(5)
    n.img_clck(GREEN_BT)
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


import random
import pygame

TILE_SIZE = 64
#%%
# function to draw the grid
window = pygame.display.set_mode(300, 300)
colour = (0,0,255) #green
circle_x_&_y = (150, 50)
circle_radius = 12
border_width = 0 #0 = filled circle

pygame.draw.circle(window, colour, circle_x_&_y, circle_radius, border_width)
#%%
import pygame
pygame.draw.line(surface, color, start_pos, end_pos, width)
#%%

0,1/min
