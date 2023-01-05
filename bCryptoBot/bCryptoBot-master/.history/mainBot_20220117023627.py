#%%

#imports



#NAVIGATE
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Navigate:
    def __init__(self):
        self.ORIGIN = os.path.join("C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\IMG\\targets") 
        self.IMG_LIST= [[x,os.path.join(self.ORIGIN, x)] for x in os.listdir(self.ORIGIN)]
        self.NAME_IMG_LIST = [x[0] for x in self.IMG_LIST]
        self.PATH_IMG_LIST = [x[1] for x in self.IMG_LIST]
        
    def getPosition(IMG=None,conf=0.8):
        position = p.locateOnScreen(image=IMG, confidence=conf)
        return position
    
    def loadPositions(self):
        
        #IMG_PATHS
        
        BLUE_BOX = os.path.join(self.ORIGIN , 'blue_box.png'),
        BROWN_BOX = os.path.join(self.ORIGIN, 'brown_box.png',)
        PURPLE_BOX = os.path.join(self.ORIGIN, 'purple_box.png',)
        REST_ALL_BUTTON = os.path.join(self.ORIGIN, 'REST_ALL_BUTTON.png',)
        REST_BUTTON = os.path.join(self.ORIGIN, 'REST_BUTTON.png',)
        SERVER_ONLINE = os.path.join(self.ORIGIN, 'SERVER_ONLINE.png',)
        TRASH = os.path.join(self.ORIGIN, 'TRASH.png',)
        T_B_BUTTON_LEFT = os.path.join(self.ORIGIN, 'T_B_BUTTON_LEFT.png',)
        T_HUNT = os.path.join(self.ORIGIN, 'T_HUNT.png',)
        T_OPEN_HERO_CASE_BUTTON = os.path.join(self.ORIGIN, 'T_OPEN_HERO_CASE_BUTTON.png',)
        T_START_GAME = os.path.join(self.ORIGIN, 'T_START_GAME.png',)
        WORK_ALL_BUTTON = os.path.join(self.ORIGIN, 'WORK_ALL_BUTTON.png',)
        WORK_BUTTON = os.path.join(self.ORIGIN, 'WORK_BUTTON.png')
        
        LOCATE = {
                    'NAME':'BLUE_BOX','POS': self.getPosition(BLUE_BOX),
                    'NAME':'BROWN_BOX','POS': self.getPosition(BROWN_BOX),
                    'NAME':'PURPLE_BOX','POS': self.getPosition(PURPLE_BOX),
                    'NAME':'REST_ALL_BUTTON','POS': self.getPosition(REST_ALL_BUTTON),
                    'NAME':'REST_BUTTON','POS': self.getPosition(REST_BUTTON),
                    'NAME':'SERVER_ONLINE','POS': self.getPosition(SERVER_ONLINE),
                    'NAME':'TRASH','POS': self.getPosition(TRASH),
                    'NAME':'T_B_BUTTON_LEFT','POS': self.getPosition(T_B_BUTTON_LEFT),
                    'NAME':'T_HUNT','POS': self.getPosition(T_HUNT),
                    'NAME':'T_OPEN_HERO_CASE_BUTTON','POS': self.getPosition(T_OPEN_HERO_CASE_BUTTON),
                    'NAME':'T_START_GAME','POS': self.getPosition(T_START_GAME),
                    'NAME':'WORK_ALL_BUTTON','POS': self.getPosition(WORK_ALL_BUTTON),
                    'NAME':'WORK_BUTTON','POS': self.getPosition(WORK_BUTTON),
        }
        
        return LOCATE
        
        
        
    def s_size(self):
        screenWidth, screenHeight = p.size()
        return screenWidth, screenHeight
    def m_pos(self):
        currentMouseX, currentMouseY = p.position()
        return currentMouseX, currentMouseY
    def mv_to(self,x=None, y=None):
        p.moveTo(x, y)

    def single_click(self, img=None):    
        p.click(p.locateOnScreen(img, confidence=0.5))
        
        
     


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
import pyautogui as p
import time
from datetime import datetime
from datetime import timedelta
import webbrowser as w
import pandas as pd
import random as r
import os.path

nv = Navigate()

LOCATE = nv.loadPositions()
df = pd.DataFrame(LOCATE)
print(df)