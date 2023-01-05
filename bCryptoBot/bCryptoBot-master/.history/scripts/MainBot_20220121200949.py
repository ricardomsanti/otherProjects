#%%
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

from pyspark import Row

#%%
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
        self.REC_H = REC_H ,
        self.TOTAL_MIN = TOTAL_MIN ,
        self.TOTAL_HORA = TOTAL_HORA,
        self.IMG = ""
        self.setTime = ""
        self.rescueTime = ""
        self.wakeTime = ""
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
    



class Navigate:
    def __init__(self):
        self.ORIGIN = os.path.join(str(os.getcwd()),"C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\IMG\\") 
        self.IMG_LIST= [[x,os.path.join(self.ORIGIN, x)] for x in os.listdir(self.ORIGIN)]
        
    def getPosition(self, IMG=None):
        position = p.locateOnScreen(image=IMG, confidence=0.8)
        return position

        
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

class Squad:
    def __init__(self, source_file = None, owner_name=None, tab_name=None):
        self.source_file = source_file
        self.owner_name = owner_name  
        self.hero_squad = []
        self.squad_owner = []
        self.tab_name = tab_name
    def load_squad(self):        
        DATA_REF = pd.read_excel(self.source_file,sheet_name=self.tab_name)
        for index, row in DATA_REF.iterrows():
            h = Hero(\
                    row['Conta'],\
                    row['ID'],\
                    row['Vida'],\
                    row['Power'],\
                    row['Speed'],\
                    row['Stamina'],\
                    row['Bomb Numb'],\
                    row['Bomb Range'],\
                    row['Extra 1'],\
                    row['Extra 2'],\
                    row['Extra 3'],\
                    row['Extra 4'],\
                    row['Extra 5'],\
                    row['CHARGE_CHECK'],\
                    row['TIPO_COMUM'],\
                    row['REC/H'],\
                    row['TOTAL_MIN'],\
                    row['TOTAL_HORA'])
            self.hero_squad.append(h)
  
        
        

#SOURCE_FILE = os.path.join(os.path.join(str(os.getcwd()),"tables",'FINAL_REFERENCE.xlsx'))
#SHEET_NAME = "REFERENCIA_FINAL"
#OWNER_NAME="Ricardo"

#HEROIS 
#DATA_REF = pd.read_excel(SOURCE_FILE,sheet_name=SHEET_NAME)
#hero_squad = DATA_REF.to_dict()





clickLt = [\
    (144,200),\
    (582,749),\
    (576,720),\
    (501,331),\
    (638,281),\
    (690,330),\
]
"""
clickLt = [ 'COORD_T_OPEN_HERO_CASE_BUTTON',\
                'COORD_IMG_T_OPEN_HERO_CASE_BUTTON',\
                'COORD_IMG_WORK_ALL_BUTTON',\
                'COORD_EXIT_BT',\
                'COORD_EXIT_BT',\
                'COORD_EXIT_BT']
"""
hero_squad
#%%
def clickTime(clickList = None, pauseTime=1):
    for x,y in clickList:
        p.click(x, y)
        t.sleel(pauseTime)
clickTime(clickList=clickLt,pauseTime=1)