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
        self.ORIGIN_PATH = ""
        self.IMG_LIST = ""
        self.NAME_IMG_LIST = ""
        self.PATH_IMG_LIST = ""
        self.BLUE_BOX_IMG = ""
        self.BROWN_BOX_IMG = ""
        self.PURPLE_BOX_IMG = ""
        self.REST_ALL_BUTTON_IMG = ""
        self.REST_BUTTON_IMG = ""
        self.SERVER_ONLINE_IMG = ""
        self.TRASH_IMG = ""
        self.T_B_BUTTON_LEFT_IMG = ""
        self.T_HUNT_IMG = ""
        self.T_OPEN_HERO_CASE_BUTTON_IMG = ""
        self.T_START_GAME_IMG = ""
        self.WORK_ALL_BUTTON_IMG = ""
        self.WORK_BUTTON_IMG = ""
        
    def load_ref(self):
        try:  
            self.ORIGIN_PATH = "C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\IMG\\targets"
            #self.IMG_LIST= [[x,os.path.join(self.ORIGIN_PATH, x)] for x in os.listdir(self.ORIGIN_PATH)]
            #self.NAME_IMG_LIST = [x[0] for x in self.IMG_LIST]
            #self.PATH_IMG_LIST = [x[1] for x in self.IMG_LIST]
            
            
            BLUE_BOX_IMG = [x for x in [x[1] for x in [[x,os.path.join(self.ORIGIN_PATH, x)] for x in os.listdir(self.ORIGIN_PATH)] if 'BLUE_BOX_IMG' in x]
            BROWN_BOX_IMG = [ x for x in [x[1] for x in [[x,os.path.join(self.ORIGIN_PATH, x)] for x in os.listdir(self.ORIGIN_PATH)] if 'BROWN_BOX_IMG' in x]
            PURPLE_BOX_IMG = [ x for x in [x[1] for x in [[x,os.path.join(self.ORIGIN_PATH, x)] for x in os.listdir(self.ORIGIN_PATH)] if 'PURPLE_BOX_IMG' in x]
            REST_ALL_BUTTON_IMG = [ x for x in [x[1] for x in [[x,os.path.join(self.ORIGIN_PATH, x)] for x in os.listdir(self.ORIGIN_PATH)] if 'REST_ALL_BUTTON_IMG' in x]
            REST_BUTTON_IMG = [ x for x in [x[1] for x in [[x,os.path.join(self.ORIGIN_PATH, x)] for x in os.listdir(self.ORIGIN_PATH)] if 'REST_BUTTON_IMG' in x]
            SERVER_ONLINE_IMG = [ x for x in [x[1] for x in [[x,os.path.join(self.ORIGIN_PATH, x)] for x in os.listdir(self.ORIGIN_PATH)] if 'SERVER_ONLINE_IMG' in x]
            TRASH_IMG = [ x for x in [x[1] for x in [[x,os.path.join(self.ORIGIN_PATH, x)] for x in os.listdir(self.ORIGIN_PATH)] if 'TRASH_IMG' in x]
            T_B_BUTTON_LEFT_IMG = [ x for x in [x[1] for x in [[x,os.path.join(self.ORIGIN_PATH, x)] for x in os.listdir(self.ORIGIN_PATH)] if 'T_B_BUTTON_LEFT_IMG' in x]
            T_HUNT_IMG = [ x for x in [x[1] for x in [[x,os.path.join(self.ORIGIN_PATH, x)] for x in os.listdir(self.ORIGIN_PATH)] if 'T_HUNT_IMG' in x]
            T_OPEN_HERO_CASE_BUTTON_IMG = [ x for x in [x[1] for x in [[x,os.path.join(self.ORIGIN_PATH, x)] for x in os.listdir(self.ORIGIN_PATH)] if 'T_OPEN_HERO_CASE_BUTTON_IMG' in x]
            T_START_GAME_IMG = [ x for x in [x[1] for x in [[x,os.path.join(self.ORIGIN_PATH, x)] for x in os.listdir(self.ORIGIN_PATH)] if 'T_START_GAME_IMG' in x]
            WORK_ALL_BUTTON_IMG = [ x for x in [x[1] for x in [[x,os.path.join(self.ORIGIN_PATH, x)] for x in os.listdir(self.ORIGIN_PATH)] if 'WORK_ALL_BUTTON_IMG' in x]
            WORK_BUTTON_IMG = [ x for x in [x[1] for x in [[x,os.path.join(self.ORIGIN_PATH, x)] for x in os.listdir(self.ORIGIN_PATH)] if 'WORK_BUTTON_IMG' in x]
        
            print("REFERENCES OK")
        except:
            print("REFERENCE ERROR")
        
        
        
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
     
#%%


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

