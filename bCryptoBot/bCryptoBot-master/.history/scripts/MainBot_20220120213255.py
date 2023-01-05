#%%dcdcdc
#imports
import pyautogui as p
import time as t
from datetime import datetime
from datetime import timedelta
import webbrowser as w
import pandas as pd
import random as r

import os
import pyautogui as p
import time as t
from datetime import datetime
from datetime import timedelta
import webbrowser as w
       
       
       
import pandas as pd
import os
  

#NAVIGATE
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Navigate:
    def __init__(self):
        self.ORIGIN = os.path.join("C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\IMG\\targets") 
        self.IMG_LIST= [[x,os.path.join(self.ORIGIN, x)] for x in os.listdir(self.ORIGIN)]
        
        self.SERVER_ONLINE = ""
        
        self.REST_ALL_BUTTON = (956,391)
        self.REST_BUTTON = ""
           
        self.WORK_BUTTON = ""
        self.WORK_ALL_BUTTON = (878,383)
        
        self.BACK_BT = (434,226)
        self.T_HUNT = (977,573)
        self.OPEN_BT = (969,900) 
        self.T_START_GAME = ""
        self.EXIT_BT = (1054,320)
        
    def getPosition(self, IMG=None):
        position = p.locateOnScreen(image=IMG, confidence=0.8)
        return position
    
    def loadPositions(self):
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
        
                    'BLUE_BOX': BLUE_BOX,
                    'BROWN_BOX': BROWN_BOX,
                    'PURPLE_BOX': PURPLE_BOX,
                    'REST_ALL_BUTTON': REST_ALL_BUTTON,
                    'REST_BUTTON': REST_BUTTON,
                    'SERVER_ONLINE': SERVER_ONLINE,
                    'TRASH': TRASH,
                    'T_B_BUTTON_LEFT': T_B_BUTTON_LEFT,
                    'T_HUNT': T_HUNT,
                    'T_OPEN_HERO_CASE_BUTTON': T_OPEN_HERO_CASE_BUTTON,
                    'T_START_GAME': T_START_GAME,
                    'WORK_ALL_BUTTON': WORK_ALL_BUTTON,
                    'WORK_BUTTON': WORK_BUTTON,
                }
        
    def s_size(self):
        screenWidth, screenHeight = p.size()
        return screenWidth, screenHeight
    def m_pos(self):
        currentMouseX, currentMouseY = p.position()
        return currentMouseX, currentMouseY
    def mv_to(self,x=None, y=None):
        p.moveTo(x, y)

    def single_click(self, POS=None):    
        p.click(POS)
        
    def tempoInicial(self):
        t0 = datetime.now()
        running_time = input("Running time?...\n")
        t1 = t0 + timedelta(hours=int(running_time))
        print(f"THIS APP WILL RUN UNTIL {t1}")
        
    def refreshArena(self):
        self.single_click(self.BACK_BT)
        t.sleep(1)
        self.single_click(self.T_HUNT)
        
    def webStart(self):
        url = "https://bombcrypto.io/"
        w.WindowsDefault(url)
        w.open(url)

    def workAll(self,pause_time=0):
        #self.single_click(self.T_HUNT)
        #print("T_HUNT")
        t.sleep(pause_time)
        self.single_click(self.OPEN_BT)
        print("OPEN_BT")
        t.sleep(pause_time)
        self.single_click(self.OPEN_BT)
        print("OPEN_BT")
        t.sleep(pause_time)
        self.single_click(self.WORK_ALL_BUTTON)
        print("WORK_ALL")
        t.sleep(pause_time)
        self.single_click(self.EXIT_BT)
        print("EXIT")
        self.single_click(self.EXIT_BT)
        t.sleep(pause_time)
        self.single_click(self.EXIT_BT)
        print("EXIT")
        
    def restAll(self,pause_time=0):
        
        self.single_click(self.T_HUNT)
        print("T_HUNT")
        t.sleep(pause_time)
        self.single_click(self.OPEN_BT)
        print("OPEN_BT")
        t.sleep(pause_time)
        self.single_click(self.OPEN_BT)
        print("OPEN_BT")
        t.sleep(pause_time)
        self.single_click(self.REST_ALL_BUTTON)
        print("WORK_ALL")
        t.sleep(pause_time)
        self.single_click(self.EXIT_BT)
        print("EXIT")
        t.sleep(pause_time)
        self.single_click(self.EXIT_BT)
        print("EXIT")
        
    def keepRunning(self):
        print("INICIANDO SEQUÊNCIA\n")
        
        t.sleep(2)
        pause_time = 2
        waitForNext = 2
        delta = 0
        x = 1
        #RODAR INDEFINIDAMENTE
        t0 = datetime.now()
        while x == 1:
            t1 = datetime.now()
            print(f"TEMPO INICIAL IGUAL A {t1}")
            delta = t1 - t0
            #RODAT ATÉ QUE
            if delta.seconds < 25:
                print("ATIVAÇÃO EM PROGRESSO")
                self.workAll(pause_time=pause_time)
                print("PAUSA")
                self.refreshArena()
                print("RENOVAÇÃO_PÁGINA")
                t.sleep(waitForNext)
                self.refreshArena()
                print("PAUSA")
                t.sleep(waitForNext)
                print("DESATIVAÇÃO EM PROGRESSO")
                self.restAll(pause_time=pause_time)
                self.refreshArena()
                t.sleep(waitForNext)
                self.refreshArena()
                t.sleep(waitForNext)
                self.refreshArena()
                t.sleep(waitForNext)
                t1 = datetime.now()
                delta = t1 - t0
                #REALIZADA A CONDICAO
            elif delta.seconds > 25*60:
                break



#################################################################################


############################################################################################################
class Hero:
    def __init__(self, \
                Conta = None,\
                ID = None,\
                Vida = None,\
                Power = None,\
                Speed = None,\
                Stamina = None,\
                BombNumb = None,\
                BombRange = None,\
                Extra1 = None,\
                Extra2 = None,\
                Extra3 = None,\
                Extra4 = None,\
                Extra5 = None,\
                CHARGE_CHECK = None,\
                TIPO_COMUM = None,\
                REC_H = None,\
                TOTAL_MIN = None,\
                TOTAL_HORA = None):
        self.Conta = Conta ,
        self.ID = ID ,
        self.Vida = Vida ,
        self.Power = Power ,
        self.Speed = Speed ,
        self.Stamina = Stamina ,
        self.BombNumb = BombNumb ,
        self.BombRange = BombRange ,
        self.Extra1 = Extra1 ,
        self.Extra2 = Extra2 ,
        self.Extra3 = Extra3 ,
        self.Extra4 = Extra4 ,
        self.Extra5 = Extra5 ,
        self.CHARGE_CHECK = CHARGE_CHECK ,
        self.TIPO_COMUM = TIPO_COMUM ,
        self.REC_H = REC_H ,
        self.TOTAL_MIN = TOTAL_MIN ,
        self.TOTAL_HORA = TOTAL_HORA,
        self.IMG = ""
        self.setTime = ""
        self.rescueTime = ""
        self.wakeTime = ""
    
    def setHero():
        
        pass
    def rescueHer():
        pass
        
    """
    def getImg(self):
        IMG_PATH = "C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\HERO_IMG"
        for x in os.listdi
    """







#######################################################################################
SQUAD_SOURCE_FILE = "C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\FINAL_REFERENCE.xlsx"   


#LOAD_SQUAD
squad = Squad(source_file=SQUAD_SOURCE_FILE,owner_name="Ricardo",tab_name='TARGET_REFERENCE')
squad.owner_name

#NAVIGATION
n=Navigate


