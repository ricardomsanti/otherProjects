
# %%


from lib2to3.pgen2.token import OP
import keyboard
from numpy import outer
import pyautogui as p
import time as t
from datetime import datetime
from datetime import timedelta
import webbrowser as w
import pandas as pd
import random as r
import webbrowser as w
import pandas as pd
import os
from PIL import Image
from cv2 import sqrt
import win32gui, win32ui, win32api, win32con
import random as r
from alive_progress import alive_bar
from win32api import GetSystemMetrics

        

    
class Aim:
    def __init__(self):
        self.dc = win32gui.GetDC(0)
        self.dcObj = win32ui.CreateDCFromHandle(self.dc)
        self.hwnd = win32gui.WindowFromPoint((0,0))
        self.monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))
        self.green = win32api.RGB(0,255, 0)
        self.black = win32api.RGB(0,0, 0)
        self.past_coordinates = self.monitor
        self.rect = win32gui.CreateRoundRectRgn(*self.past_coordinates, 2 , 2)
        win32gui.RedrawWindow(self.hwnd, self.past_coordinates, self.rect, win32con.RDW_INVALIDATE)
        self.s_mode = 1
        
    def runAim(self, time=4, reference=0, mode='auto',size=50):
        t0 = datetime.now()
        delta = timedelta(seconds=time)
        t1 = t0 + delta
        pos = reference
        while t1 > t0:
            if  mode == 'auto':
                pos = p.position()
            else:
                pos = reference
                
            rect = win32gui.CreateRoundRectRgn(*self.past_coordinates, 2 , 2)
            win32gui.RedrawWindow(self.hwnd, self.past_coordinates, self.rect, win32con.RDW_INVALIDATE)
            
            for y in range(-size,size,1):
                n = 50
                z = n-2
                #line ||
                win32gui.SetPixel(self.dc, pos[0]-n, pos[1]+y, self.green)
                win32gui.SetPixel(self.dc, pos[0]+n, pos[1]+y, self.green)
                #line =
                win32gui.SetPixel(self.dc, pos[0] + y, pos[1]+n, self.green)
                win32gui.SetPixel(self.dc, pos[0]+ y, pos[1]-n,self.green)

                #line ||
                win32gui.SetPixel(self.dc, pos[0]-(n-1), pos[1]+y, self.black)
                win32gui.SetPixel(self.dc, pos[0]+(n-1), pos[1]+y, self.black)
                #line =
                win32gui.SetPixel(self.dc, pos[0] + y, pos[1]+(n-1), self.black)
                win32gui.SetPixel(self.dc, pos[0]+ y, pos[1]-(n-1), self.black)

          
                
            t0 = datetime.now()   
            self.past_coordinates = (pos[0]-40, pos[1]-40, pos[0]+40, pos[1]+40)

    def runLine(self, time=4, reference=0, mode='auto',size=300):
        t0 = datetime.now()
        delta = timedelta(seconds=time)
        t1 = t0 + delta
        pos = reference
        while t1 > t0:
            if  mode == 'auto':
                pos = p.position()
            else:
                pos = reference
                
            rect = win32gui.CreateRoundRectRgn(*self.past_coordinates, 2 , 2)
            win32gui.RedrawWindow(self.hwnd, self.past_coordinates, self.rect, win32con.RDW_INVALIDATE)
            for y in range(-size,size,1):
                #line ||
                win32gui.SetPixel(self.dc, pos[0], pos[1]+y, self.green)
                win32gui.SetPixel(self.dc, pos[0], pos[1]+y, self.green)
                #line =
                win32gui.SetPixel(self.dc, pos[0] + y, pos[1], self.green)
                win32gui.SetPixel(self.dc, pos[0]+ y, pos[1],self.green)

                
                
            t0 = datetime.now()   
            self.past_coordinates = (pos[0]-40, pos[1]-40, pos[0]+40, pos[1]+40)

    def runDoubleAim(self):
        self.runLine(time=0.5, size=200)
        self.runAim(time=0.5,size=25)
        
    def findTargets(self, targetList = []):
        for pos in targetList:
            self.runAim(time=2, pos=pos)

class Cryptus:
    def __init__(self, BC_CRD=None,\
        BLUE_BOX_CRD=None,\
        BROWN_BOX_CRD=None,\
        OPEN_CRD=None,\
        PURPLE_BOX_CRD=None,\
        RA_CRD=None,\
        TH_CRD=None,\
        WA_CRD=None,\
        WARRIOR_CRD=None,\
        EX_CRD= None):

        self.BC_CRD = BC_CRD
        self.BLUE_BOX_CRD = BLUE_BOX_CRD
        self.BROWN_BOX_CRD = BROWN_BOX_CRD
        self.OPEN_CRD = OPEN_CRD
        self.PURPLE_BOX_CRD = PURPLE_BOX_CRD
        self.RA_CRD = RA_CRD
        self.TH_CRD = TH_CRD
        self.WA_CRD = WA_CRD
        self.WARRIOR_CRD = WARRIOR_CRD
        self.EX_CRD = EX_CRD
        
        self.aim = Aim()
        self.targetList = []
        self.logo = """
        

            ==============================================================================================
                    ||
            --------||-Kryptus      
            --------||----1.0
            --------||---------------
            ==============================================================================================
                   """

    #ASSEGURAR JANELA PRINCIPAL SELECIONADA

    def activeWindowSelection(self):
        print("Press 's' to stop")
        while keyboard.is_pressed("s") == False:
            self.activeWindow = p.getActiveWindowTitle()
            print(self.activeWindow)
            t.sleep(1)
            if keyboard.is_pressed("s"):
                break
        print(f"Active Window : {self.activeWindow}") 
    
    #CLICAR EM UM ALVO

    def ckTarget(self, target=None,\
         time=2, conf=0.6):
            try:
                t.sleep(time)
                t.sleep(1)
                p.moveTo(target[0], target[1])
                self.aim.runDoubleAim()
                p.click()
                t.sleep(time)
            except:
                print(f"algo deu errado quando clincando no item {target}")    
         

    def openHeroCase(self):
        self.ckTarget(self.OPEN_CRD)
        self.ckTarget(self.WARRIOR_CRD)



    def actionAll(self,pause_time=2, mode='WA'):
        self.openHeroCase()
        if mode == "WA":
            self.ckTarget(self.WA_CRD)
            self.ckTarget(self.EX_CRD)
            self.ckTarget(self.BC_CRD)
            self.ckTarget(self.TH_CRD)
        elif mode == "RA":
            self.ckTarget(self.RA_CRD)
            self.ckTarget(self.EX_CRD)
            self.ckTarget(self.BC_CRD)
            self.ckTarget(self.TH_CRD)

   
  
    def keepRunning(self, limit = 3,t1=1, t2=1):
        #alternar as rotinas worKlall e rest all por um determinado tempo
        
        counter = 0
        while limit > counter:
            self.actionAll(mode="WA")
            t.sleep(t1)
            self.actionAll(mode="RA")
            t.sleep(t2)
            counter += 1
            if counter > limit:
                print("SEQUENCIA FINALIZADA")
                break
                
            
    def refreshArena(self):
        p.click()
        BC = Image.open(self.references['BC_IMG'])
        TH = Image.open(self.references['TH_IMG'])
        self.ckTarget(target=BC)
        self.ckTarget(target=TH)
    
    

    def checkButtons(self):

        while recon_check != 1:
            recon_full = [x for x in check_list.values()]
            recon = [x for x in check_list.values() if p.locateOnScreen(x, confidence=0.6) != None]
            print(f"Reconhecidos: {len(recon)}/{len(recon_full)}")
            recon_check = len(recon)/len(recon_full) 
            check_list = c.references 

            recon_check = 0
            for x, y in check_list.items():
                try:
                    position = p.locateOnScreen(y, confidence=0.6)
                    if position != None:
                        posit_coord = p.center(position)
                        print(f"Encontrado: {x}")
                        print(f"Coordenadas: {posit_coord[0]},{posit_coord[1]}")
                        t.sleep(1)
                        p.moveTo(posit_coord[0],posit_coord[1])
                        self.aim.runAim(mode='manual',time=4 ,reference=posit_coord)
                        check_list[x] = {"FOUND"}
                    else:
                        print(f"------Pending items:")
                except:
                    print(f"Cound not locate image: {x}")

    def getReference(self, pos_list = []):
        x_locator = 1
        i= ""
        while x_locator == 1:
            confirm = input("Registrar novo ponto?")
            if confirm=="s":
                COORD = p.position()
                NAME = input("Nome da referência:")
                pos_list.append([COORD,NAME])
                confirm = input("Registrar novo ponto?")
                if confirm == "s":
                    self.getReference(pos_list=pos_list)
                else:
                    break
            else:
                x_locator = 0       
        return pos_list

class Conf:
    def __init__(self):
        self.BC_CRD = ""
        self.BLUE_BOX_CRD = ""
        self.BROWN_BOX_CRD = ""
        self.OPEN_CRD = ""
        self.PURPLE_BOX_CRD = ""
        self.RA_CRD = ""
        self.TH_CRD = ""
        self.WA_CRD = ""
        self.WARRIOR_CRD = ""
        self.EX_CRD = ""
        self.CRD_LIST = ""
        self.activeWindow = ""

    def mainPreConf(self, target=None):
        print("=====================================================")   
        target_string = str(target)
        text =f"GRAVAR ALVO {str(target_string)}"
        record = p.confirm(title="SETUP", text=text ,button=["OK", "STOP"])
        if record == 'ok':
            for x in [3,2,1,"ok"]:
                t.sleep(1)
                print(x)
            position = p.position()
            t.sleep(2)
        target = position
        
    def listConf(self):
        conf_list = []
        conf_list.append(self.BC_CRD)
        conf_list.append(self.BLUE_BOX_CRD)
        conf_list.append(self.BROWN_BOX_CRD)
        conf_list.append(self.OPEN_CRD)
        conf_list.append(self.PURPLE_BOX_CRD)
        conf_list.append(self.RA_CRD)
        conf_list.append(self.TH_CRD)
        conf_list.append(self.WA_CRD)
        conf_list.append(self.WARRIOR_CRD)
        conf_list.append(self.EX_CRD)
        return conf_list
    def mainConf(self):

        print("CALIBRANDO ALVOS\n")
        print("=====================================================")      
        
        self.BC_CRD = self.mainPreConf("BC_CRD") 
        self.BLUE_BOX_CRD = self.mainPreConf("BLUE_BOX_CRD") 
        self.BROWN_BOX_CRD = self.mainPreConf("BROWN_BOX_CRD") 
        self.OPEN_CRD = self.mainPreConf("OPEN_CRD") 
        self.PURPLE_BOX_CRD = self.mainPreConf("PURPLE_BOX_CRD") 
        self.RA_CRD = self.mainPreConf("RA_CRD") 
        self.TH_CRD = self.mainPreConf("TH_CRD") 
        self.WA_CRD = self.mainPreConf("WA_CRD") 
        self.WARRIOR_CRD = self.mainPreConf("WARRIOR_CRD") 
        self.EX_CRD = self.mainPreConf("EX_CRD") 
   
   
#%%
a = Aim()
c = Cryptus()
cf = Conf()
cf.mainConf()
a.runDoubleAim()
#c.mainConf()
cf.listConf()

#c.activeWindowSelection()
#c.keepRunning()


