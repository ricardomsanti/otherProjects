
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

    def ckTarget(self, target=None, time=2, conf=0.6):
            try:
                t.sleep(time)
                t.sleep(1)
                p.moveTo(target[0], target[1])
                self.aim.runDoubleAim()
                p.click()
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

   
    
    def mainConf(self):

        print("CALIBRANDO ALVOS\n")
        print("PARA MARCAR UM ALVO, COLOQUE O CURSOR SOBRE ELE E, DIGITE 'GRAVAR', DE ENTER E ESPERE AT?? QUE A MENSAGEM OK' APARE??A")
        print("=====================================================")      
        key = input("BOT??O VERDE SUPERIOR ESQUEDO\n")
        if key == "GRAVAR":
            for x in [3,2,1,"ok"]:
                print(x)
                self.BC_CRD = p.position()
                t.sleep(3)
                self.aim.runAim()
            
        key =input("EXEMPLO BA?? AZUL\n")
        
        if key == "GRAVAR":
            for x in [3,2,1,"ok"]:
                print(x)
                self.BLUE_BOX_CRD = p.position()
                t.sleep(3)
                self.aim.runAim()

        if key == "GRAVAR":
            for x in [3,2,1,"ok"]:
                self.PURPLE_BOX_CRD = p.position()
                t.sleep(3)
                self.aim.runAim()
        
        key =   = input("EXEMPLO DE SETA QUE ABRE A GAVETA DOS BONECOS\n")
        if key == "GRAVAR":
            for x in [3,2,1,"ok"]:
                print(x)
                self.OPEN_CRD   = p.position()
                t.sleep(3)
                self.aim.runAim()
    
        key = input("BOT??O DO BONECO DE ARMADURA QUE ABRE A JANELA DE CONTROLE\n")     
        if key == "GRAVAR":
            for x in [3,2,1,"ok"]:
                print(x)
                self.WARRIOR_CRD   = p.position()
                t.sleep(3)
                self.aim.runAim()
        

        key  = input("BOT??O QUE COLOCA TODOS PARA TRABALHAR\n")      
        if key == "GRAVAR":
            for x in [3,2,1,"ok"]:
                print(x)
                self.WA_CRD  = p.position()
                t.sleep(3)
                self.aim.runAim()
        

        key  = input("BOT??O CENTRAL TREASURE HUNT\n")
        if key == "GRAVAR":
            for x in [3,2,1,"ok"]:
                print(x)
                self.TH_CRD = p.position()
                t.sleep(3)
                self.aim.runAim()
        
        key =input("BOT??O QUE COLOCA TODOS PARA DESCANSAR\n")  
        if key == "GRAVAR":
            for x in [3,2,1,"ok"]:
                print(x)
                self.RA_CRD  = p.position()
                t.sleep(3)
                self.aim.runAim()
        key  = input("EXEMPLO BA?? ROXO\n") 

        key =  input("BOT??O DE SA??DA\n")    
        if key == "GRAVAR":
            for x in [3,2,1,"ok"]:
                print(x)
                self.EXIT_BUTTON =  p.position()
                t.sleep(3)
                self.aim.runAim()
        key  = input("EXEMPLO BA?? ROXO\n")   
     


              
       
       
        =     
     
        
        
      
                    
        
        
    

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


#%%
a = Aim()
c = Cryptus()
a.runDoubleAim()
c.mainConf()
c.activeWindowSelection()
c.keepRunning()


