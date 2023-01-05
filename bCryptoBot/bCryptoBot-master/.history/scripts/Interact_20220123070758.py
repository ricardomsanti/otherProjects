import pyautogui as p
import time as t
import os
from datetime import datetime as dt
from datetime import timedelta as td
import pyautogui as p
import win32gui, win32ui, win32api, win32con
from win32api import GetSystemMetrics


class Interaction:
    def __init__(self):
            self.mainRef = {
            'TH':    (997, 493 ), 
            'BC':    (539, 186 ), 
            'OPEN':  (971, 732 ),
            'OA':    (899, 322 ), 
            'RA':    (952, 323 ),   
            'RO':    (948, 362 ), 
            'WO':    (889, 368 ), 
            'H':    (662, 361) ,
            'EX':   (1029,316)
                    },
            self.BLUE_BOX_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'blue_box.png')
            self.BROWN_BOX_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'brown_box.png')
            self.PURPLE_BOX_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'purple_box.png')
            self.YELLOW_BOX_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'yellow_box.png')
            self.RA_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'RA.png')
            self.REST_BUTTON_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'REST_BUTTON.png')
            self.SERVER_ONLINE_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'SERVER_ONLINE.png')
            self.TRASH_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'TRASH.png')
            self.T_B_BUTTON_LEFT_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'T_B_BUTTON_LEFT.png')
            self.TH_IMG =  os.path.join(os.getcwd(),'IMG//targets' ,'TH.png')
            self.OPEN_IMG =  os.path.join(os.getcwd(),'IMG//targets' ,'OPEN.png')
            self.T_START_GAME_IMG =  os.path.join(os.getcwd(),'IMG//targets' ,'T_START_GAME.png')
            self.WA_IMG =  os.path.join(os.getcwd(),'IMG//targets' ,'WA.png')
            self.WORK_BUTTON_IMG=  os.path.join(os.getcwd(),'IMG//targets' ,'WORK_BUTTON.png')
            


    def findTarget(self,target):
            
        dc = win32gui.GetDC(0)
        dcObj = win32ui.CreateDCFromHandle(dc)
        hwnd = win32gui.WindowFromPoint((0,0))
        monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))
        green = win32api.RGB(0,255, 0)

        past_coordinates = monitor
        rect = win32gui.CreateRoundRectRgn(*past_coordinates, 2 , 2)
        win32gui.RedrawWindow(hwnd, past_coordinates, rect, win32con.RDW_INVALIDATE)

        past_coordinates = monitor
        

        while True:
            m = win32gui.GetCursorPos()

            rect = win32gui.CreateRoundRectRgn(*past_coordinates, 2 , 2)
            win32gui.RedrawWindow(hwnd, past_coordinates, rect, win32con.RDW_INVALIDATE)

            for x in range(10,70,1):
                win32gui.SetPixel(dc, m[0]+x, m[1], green)
                win32gui.SetPixel(dc, m[0]-x, m[1], green)
                win32gui.SetPixel(dc, m[0], m[1]+x, green)
                win32gui.SetPixel(dc, m[0], m[1]-x, green)


        
    def clickTarget(self,field=None, mode = 'click'):
        try:
            print(f"Clicando em {field}")
            t.sleep(2)
            p.click(p.locateOnScreen(self.OPEN_IMG))
        except:
            print(f"algo deu errado quando clincando no item {field}")    
        
        



        
    def refreshArena(self):
        p.click()
        self.clickTarget(field="BC", mode='click')
        self.clickTarget(field="TH", mode='click')
    
    
    def openHeroCase(self):
        
        self.clickTarget('OPEN')
        t.sleep(2)
        self.clickTarget('OPEN')
        
        
    def actionAll(self,pause_time=2, mode='WA'):
        print("OPEN")
        self.openHeroCase()
        if mode == "WA":
            self.clickTarget('DA')
        elif mode == "RA":
            self.clickTarget('RA')
            
        self.clickTarget('EX')
        self.clickTarget('EX')
  
    
    def keepRunning(self, limit = 5,t1=1, t2=3):
        
        #alternar as rotinas worlall e rest all por um determinado tempo
        
        print("INICIANDO SEQUÊNCIA\n")
        counter = 0
        while limit > counter:
            
            self.actionAll(pause_time=2,mode="WORK")
            t.sleep(t1)
            self.actionAll(self.actionAll(pause_time=2,mode="REST"))
            t.sleep(t2)
            counter += 1
            if counter > limit:
                print("SEQUENCIA FINALIZADA")
                break

    def checkRef(self):
        i= ""
        pos_list = []
        while i == "":
            confirm = input("Marcar novo ponto?")
            if confirm=="s":
                COORD = p.position()
                NAME = input("Nome da referência:")
                pos_list.append([COORD,NAME])
            elif confirm == "n":
                i= "end"
            else:
                continue
        print(pos_list)