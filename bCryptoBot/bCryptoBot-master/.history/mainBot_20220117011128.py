#%%

#imports

import pyautogui as p
import time
from datetime import datetime
from datetime import timedelta
import webbrowser as w
import pandas as pd
import random as r
import os.path

#NAVIGATE
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Navigate:
    def __init__(self):
        self.ORIGIN = os.path.join("C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\IMG\\targets") 
        self.IMG_LIST= [[x,os.path.join(self.ORIGIN, x)] for x in os.listdir(self.ORIGIN)]
        self.NAME_IMG_LIST = [x[0] for x in self.IMG_LIST]
        self.PATH_IMG_LIST = [x[1] for x in self.IMG_LIST]
        self.BLUE_BOX = os.path.join(self.ORIGIN , 'blue_box.png'),
        self.BROWN_BOX = os.path.join(self.ORIGIN, 'brown_box.png',)
        self.PURPLE_BOX = os.path.join(self.ORIGIN, 'purple_box.png',)
        self.REST_ALL_BUTTON = os.path.join(self.ORIGIN, 'REST_ALL_BUTTON.png',)
        self.REST_BUTTON = os.path.join(self.ORIGIN, 'REST_BUTTON.png',)
        self.SERVER_ONLINE = os.path.join(self.ORIGIN, 'SERVER_ONLINE.png',)
        self.TRASH = os.path.join(self.ORIGIN, 'TRASH.png',)
        self.T_B_BUTTON_LEFT = os.path.join(self.ORIGIN, 'T_B_BUTTON_LEFT.png',)
        self.T_HUNT = os.path.join(self.ORIGIN, 'T_HUNT.png',)
        self.T_OPEN_HERO_CASE_BUTTON = os.path.join(self.ORIGIN, 'T_OPEN_HERO_CASE_BUTTON.png',)
        self.T_START_GAME = os.path.join(self.ORIGIN, 'T_START_GAME.png',)
        self.WORK_ALL_BUTTON = os.path.join(self.ORIGIN, 'WORK_ALL_BUTTON.png',)
        self.WORK_BUTTON = os.path.join(self.ORIGIN, 'WORK_BUTTON.png')

        
        
    def s_size(self):
        screenWidth, screenHeight = p.size()
        return screenWidth, screenHeight
    def m_pos(self):
        currentMouseX, currentMouseY = p.position()
        return currentMouseX, currentMouseY
    def mv_to(self,x=None, y=None):
        p.moveTo(x, y)

    def single_click(self, img=None):    
        p.click(p.locateCenterOnScreen(img, confidence=0.8))
        
        
     


"""
#INTERACT
# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      
def tempoInicial():
    t0 = datetime.now()
    running_time = input("Running time?...\n")
    t1 = t0 + timedelta(hours=int(running_time))
    print(f"THIS APP WILL RUN UNTIL {t1}")
    
 
def webStart():
    url = "https://bombcrypto.io/"
    w.WindowsDefault(url)
    w.open(url)

def keepRunning():
    pass

#ESTABELECE POR QUANTO TEMPO A FUNCÃO VAI RODAR
tempoInicial()

#ABRE A URL DO JOGO NO NAVEGADOR PADRÃO DO SISTEMA
webStart()

"""

nv = Navigate()

