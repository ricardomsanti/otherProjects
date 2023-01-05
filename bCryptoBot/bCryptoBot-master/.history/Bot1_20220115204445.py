#%%

#imports

import pyautogui as p
import time
import time
from datetime import datetime
from datetime import timedelta
import webbrowser as w


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
    def get_IMG(self, x=None, y=None):
        T_HUNT  = (x,y)
        return 

class Hero:
    def __init__(self):
        self.name = ""
        self.mac_



        
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



#ESTABELECE POR QUANTO TEMPO A FUNCÃO VAI RODAR
tempoInicial()

#ABRE A URL DO JOGO NO NAVEGADOR PADRÃO DO SISTEMA
webStart()

#%%#objetos instanciados

ob1 = Objects()
ob2 = Objects()
ob1_OPEN_CASE = ob1.get_OPEN_CASE(538,740)
ob1_OPEN_CASE_CONF = ob1.get_OPEN_CASE(538,740)

ob1_get_ALL_WORK_BT= ob1.get_ALL_WORK_BT(279,257)
ob1_ALL_REST_BT = ob1.get_ALL_REST_BT(318,256)
ob1_EXIT_BUTTON = ob1.get_EXIT_BUTTON(371,223)
ob1_GREEN_BT = ob1.get_GREEN_BT(41,170)
ob1_T_HUNT = ob1.get_T_HUNT(337,347)

#%%
import pandas as pd
import random as r
import os.path
HERO_KEYS = [ "ID",\
                "POWER",\
                "SPEED",\
                "STAMIN",\
                "BOMB_NUM",\
                "BOMB_RANGE",\
                "LIFE"]
#%%
HEROE = {x:r.randint(1,10) for x in HERO_KEYS}


HEROES_LIST = 


HERO_ROUNDS = { x:[{x:r.randint(1,10) for x in HERO_KEYS} for x in range(15)] for x in range(1000)}
df = pd.DataFrame(HEROES_LIST)
df.to_csv("dash.csv")

