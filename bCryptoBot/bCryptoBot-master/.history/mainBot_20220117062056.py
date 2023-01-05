#%%

#imports
import pyautogui as p
import time as t
from datetime import datetime
from datetime import timedelta
import webbrowser as w
import pandas as pd
import random as r
import os.path

#
#NAVIGATE
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Navigate:
    def __init__(self):
        self.ORIGIN = os.path.join("C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\IMG\\targets") 
        self.IMG_LIST= [[x,os.path.join(self.ORIGIN, x)] for x in os.listdir(self.ORIGIN)]
        self.NAME_IMG_LIST = [x[0] for x in self.IMG_LIST]
        self.PATH_IMG_LIST = [x[1] for x in self.IMG_LIST]
        self.SERVER_ONLINE = ""
        
        self.REST_ALL_BUTTON = (956,391)
        self.REST_BUTTON = ""
        
        self.WORK_BUTTON = ""
        self.WORK_ALL_BUTTON = (878,383)
        
        self.BACK_BT = (434,226)
        self.T_HUNT = (977,573)
        self.OPEN_BT = (969,900) 
        self.T_START_GAME = ""
        self.EXIT_BT = (1028,335)
        
    def getPosition(self, IMG=None):
        position = p.locateOnScreen(image=IMG, confidence=0.8)
        return position
    
    def loadPositions(self):
        
        """
        #IMG_PATHS
        
        #BLUE_BOX_POS = ""
        #BROWN_BOX_POS = ""
        #PURPLE_BOX_POS = ""
        
        SERVER_ONLINE_POS = ""
        
        #TRASH_POS = ""
        T_B_BUTTON_LEFT_POS = ""
        T_HUNT_POS = ""
        T_OPEN_HERO_CASE_BUTTON_POS = ""
        T_START_GAME_POS = ""
        
        
        REST_BUTTON_POS = ""
        REST_ALL_BUTTON_POS = ""

        WORK_BUTTON_POS = ""
        WORK_ALL_BUTTON_POS = (279,257)
        
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
        
        LOCATE = {}
        
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
        """
        
        
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
        
    
    def webStart(self):
        url = "https://bombcrypto.io/"
        w.WindowsDefault(url)
        w.open(url)

    def workAll(self,pause_time=0):
        self.single_click(self.T_HUNT)
        print("T_HUNT")
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
        self.EXIT_BT = (1028,335)
        print("EXIT")
        t.sleep(pause_time)
        self.EXIT_BT = (1028,335)
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
        self.EXIT_BT = (1028,335)
        print("EXIT")
        t.sleep(pause_time)
        self.EXIT_BT = (1028,335)
        print("EXIT")
        
        
    def keepRunning(self):
        t.sleep(2)
        pause_time = 2
        recovery_time = 240
        delta = 0
        x = 1
        turn = 0
        #RODAR INDEFINIDAMENTE
        while x == 1:
            t0 = datetime.now()
            t.sleep(1)
            t1 = datetime.now()
            delta = t1 - t0
            
            #RODAT ATÉ QUE
            while delta.seconds <180:
                self.workAll(pause_time=pause_time)
                t.sleep(45)
                t1 = datetime.now()
                delta = t1 - t0
                #REALIZADA A CONDICAO
                if delta.seconds > 120:
                    self.restAll(pause_time=pause_time)
                    t.sleep(5)
                    break
            """
            self.workAll(pause_time=pause_time)
            t.sleep(3)
            self.workAll(pause_time=pause_time)
            t.sleep(3)
            self.restAll(pause_time=pause_time)
            t.sleep(10)
            
#ESTABELECE POR QUANTO TEMPO A FUNCÃO VAI RODAR
nv = Navigate()
nv.keepRunning()

#ABRE A URL DO JOGO NO NAVEGADOR PADRÃO DO SISTEMA
#nv.webStart()
