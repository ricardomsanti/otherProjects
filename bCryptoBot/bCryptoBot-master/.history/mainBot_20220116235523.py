#%%

#imports

import pyautogui as p
import time
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
        self.cwd = os.path.cwd()
        self.ORIGIN_PATH = "C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\IMG\\targets"
        self.IMG_LIST= [[x,os.path.join(self.ORIGIN_PATH, x)] for x in os.listdir(self.ORIGIN_PATH)]
        self.NAME_IMG_LIST = [x[0] for x in self.IMG_LIST]
        self.PATH_IMG_LIST = [x[1] for x in self.IMG_LIST]
        self.BLUE_BOX = os.path.join(self.cdw,'blue_box.png')
        self.BROWN_BOX = 'C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\IMG\\targets\\brown_box.png',
        self.PURPLE_BOX = 'C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\IMG\\targets\\purple_box.png',
        self.REST_ALL_BUTTON = 'C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\IMG\\targets\\REST_ALL_BUTTON.png',
        self.REST_BUTTON = 'C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\IMG\\targets\\REST_BUTTON.png',
        self.SERVER_ONLINE = 'C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\IMG\\targets\\SERVER_ONLINE.png',
        self.TRASH = 'C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\IMG\\targets\\TRASH.png',
        self.T_B_BUTTON_LEFT = 'C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\IMG\\targets\\T_B_BUTTON_LEFT.png',
        self.T_HUNT = 'C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\IMG\\targets\\T_HUNT.png',
        self.T_OPEN_HERO_CASE_BUTTON = 'C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\IMG\\targets\\T_OPEN_HERO_CASE_BUTTON.png',
        self.T_START_GAME = 'C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\IMG\\targets\\T_START_GAME.png',
        self.WORK_ALL_BUTTON = 'C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\IMG\\targets\\WORK_ALL_BUTTON.png',
        self.WORK_BUTTON = 'C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\IMG\\targets\\WORK_BUTTON.png'

        
    def load_ref(self):
        pass
        
        
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
    def mvt_click(self,x=None, y=None):
        p.click(x, y)
        
    def img_click(img=None):
        p.click(img)
     


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

