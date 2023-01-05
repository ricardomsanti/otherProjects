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
        
    def getPosition(IMG=None):
        position = p.locateOnScreen(image=IMG, confidence=0.8)
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
                    'BLUE_BOX': self.getPosition(BLUE_BOX),
                    'BROWN_BOX': self.getPosition(BROWN_BOX),
                    'PURPLE_BOX': self.getPosition(PURPLE_BOX),
                    'REST_ALL_BUTTON': self.getPosition(REST_ALL_BUTTON),
                    'REST_BUTTON': self.getPosition(REST_BUTTON),
                    'SERVER_ONLINE': self.getPosition(SERVER_ONLINE),
                    'TRASH': self.getPosition(TRASH),
                    'T_B_BUTTON_LEFT': self.getPosition(T_B_BUTTON_LEFT),
                    'T_HUNT': self.getPosition(T_HUNT),
                    'T_OPEN_HERO_CASE_BUTTON': self.getPosition(T_OPEN_HERO_CASE_BUTTON),
                    'T_START_GAME': self.getPosition(T_START_GAME),
                    'WORK_ALL_BUTTON': self.getPosition(WORK_ALL_BUTTON),
                    'WORK_BUTTON': self.getPosition(WORK_BUTTON),
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