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
        
        self.REST_ALL_BUTTON = ""
        self.REST_BUTTON = ""
        
        self.WORK_BUTTON = ""
        self.WORK_ALL_BUTTON = (878,383)
        
        self.BACK_BT = (434,226)
        self.T_HUNT = (977,573)
        self.OPEN_BT = (969,900) 
        self.T_START_GAME = ""
        
        
    def getPosition(IMG=None):
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

"""

TUDO COME??A "CHAMANDO A CLASSE QUE TEM TODAS AS FERRAMENTA QUE VC VAI PRECISAR"
nv = Navigate()

PRA ABRIR A CAIXA USAMOS O PONTO(.)

O M??TODO PARA CLICAR EM ALGO PRECISA DE UM PAR??METRO PARA FUNCIONAR

nv.single_click(....)

AS CORDENADAS EST??O SALVAS DENTRO DA CAIXA TAMB??M
EXEMPLO:

nv.T_HUNT.....coordenadas do bot??o que abre o tabuleiro

"""

#ESTABELECE POR QUANTO TEMPO A FUNC??O VAI RODAR
#nv.tempoInicial()

#ABRE A URL DO JOGO NO NAVEGADOR PADR??O DO SISTEMA
#nv.webStart()

#
nv.single_click(nv.T_HUNT)
t.sleep(2)
nv.