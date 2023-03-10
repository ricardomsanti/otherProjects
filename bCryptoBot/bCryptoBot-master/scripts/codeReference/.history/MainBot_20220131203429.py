
# %%

#%%

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
    def __init__(self):
        self.references = { 'BC_IMG' : 'IMG_BC.png',
                'BLUE_BOX_IMG' : 'IMG_blue_box.png',
                'BROWN_BOX_IMG' : 'IMG_brown_box.png',
                'OPEN_IMG' : 'IMG_OPEN.png',
                'PURPLE_BOX_IMG' : 'IMG_purple_box.png',
                'RA_IMG' : 'IMG_RA.png',
                'RAO_IMG' : 'IMG_RAO.png',
                'SG_IMG' : 'IMG_SG.png',
                'SO_IMG' : 'IMG_SO.png',
                'TH_IMG' : 'IMG_TH.png',
                'TRASH_IMG' : 'IMG_TRASH.png',
                'WA_IMG' : 'IMG_WA.png',
                'WAO_IMG' : 'IMG_WAO.png',
                'BC_IMG' : 'IMG_BC.png',
                'WARRIOR_IMG' :'IMG_WARRIOR.png',
                'EX_IMG' :'IMG_EX.png'}
        self.BC_IMG = ""
        self.BLUE_BOX_CRD = "",
        self.BROWN_BOX_CRD = "",
        self.OPEN_CRD = "",
        self.PURPLE_BOX_CRD = "",
        self.RA_CRD = "",
        self.RAO_CRD = "",
        self.SG_CRD = "",
        self.SO_CRD = "",
        self.TH_CRD = "",
        self.TRASH_CRD = "",
        self.WA_CRD = "",
        self.WAO_CRD = "",
        self.BC_CRD = "",
        self.WARRIOR_CRD = "",
        self.EX_CRD = ""}
        self.BC_IMG = self.references['BC_IMG']
        self.BLUE_BOX_IMG = self.references['BLUE_BOX_IMG']
        self.BROWN_BOX_IMG = self.references['BROWN_BOX_IMG']
        self.OPEN_IMG = self.references['OPEN_IMG']
        self.PURPLE_BOX_IMG = self.references['PURPLE_BOX_IMG']
        self.RA_IMG = self.references['RA_IMG']
        self.RAO_IMG = self.references['RAO_IMG']
        self.SG_IMG = self.references['SG_IMG']
        self.SO_IMG = self.references['SO_IMG']
        self.TH_IMG = self.references['TH_IMG']
        self.TRASH_IMG = self.references['TRASH_IMG']
        self.WA_IMG = self.references['WA_IMG']
        self.WAO_IMG = self.references['WAO_IMG']
        self.BC_IMG = self.references['BC_IMG']
        self.WARRIOR_IMG = self.references['WARRIOR_IMG']
        self.EX_IMG = self.references['EX_IMG']
        self.activeWindow = ""
        self.aim = Aim()
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

    def ckTarget(self,mode='click',target=None, time=2, conf=0.6):
            if mode == "click":
                t.sleep(time)
                print(f"Clicando em {target}")
                loc = p.locateOnScreen(target, confidence=conf)
                print("localizado")
                center = p.center(loc)
                t.sleep(1)
                p.moveTo(center[0], center[1])
                self.aim.runDoubleAim()
                t.sleep(1)
                p.click()
                print(f"algo deu errado quando clincando no item {target}")    
         

    def openHeroCase(self):
        self.ckTarget(self.OPEN_IMG)
        self.ckTarget(self.WARRIOR_IMG)



    def actionAll(self,pause_time=2, mode='WA'):
        self.openHeroCase()
        if mode == "WA":
            self.ckTarget(self.WA_IMG)
            self.ckTarget(self.EX_IMG)
            self.ckTarget(self.BC_IMG)
            self.ckTarget(self.TH_IMG)
        elif mode == "RA":
            self.ckTarget(self.RA_IMG)
            self.ckTarget(self.EX_IMG)
            self.ckTarget(self.BC_IMG)
            self.ckTarget(self.TH_IMG)

    def confAll(self):
        self.cord_references
        t.sleep(2)
        for x, y in self.cord_references.items():
            print(f"Mantenha o mouse sobre o alvo {x} por 5 seg")
            coord = p.center(p.position())
            self.coord_references[x] = coord
            next = input(f"Coordenadas de {coord} gravadas. Seguir para a pr??xima?(y/n)")
            if next == "n":
                break
        
    

    def keepRunning(self, limit = 3,t1=1, t2=1):
        #alternar as rotinas worKlall e rest all por um determinado tempo
        
        print("INICIANDO SEQU??NCIA\n")
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
                NAME = input("Nome da refer??ncia:")
                pos_list.append([COORD,NAME])
                confirm = input("Registrar novo ponto?")
                if confirm == "s":
                    self.getReference(pos_list=pos_list)
                else:
                    break
            else:
                x_locator = 0       
        return pos_list

a = Aim()
a.runDoubleAim()

# %%

# %%

# %%

# %%

# %%

#%%
c = Cryptus()
c.activeWindowSelection()
c.keepRunning()
