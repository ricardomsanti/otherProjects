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

"""

    #MOUSE_FUNCTIONS
    screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
    currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
    pyautogui.moveTo(100, 150) # Move the mouse to the x, y coordinates 100, 150.
    pyautogui.click() # Click the mouse at its current location.
    pyautogui.click(200, 220) # Click the mouse at the x, y coordinates 200, 220.
    pyautogui.doubleClick() # Double click the mouse at the
    pyautogui.write('Hello world!', interval=0.25)  # Type with quarter-second pause in between each key.
    pyautogui.press('esc') # Simulate pressing the Escape key.
    
    #BUTTON_FUNCTION
     buttonx, buttony = pyautogui.locateCenterOnScreen('button.png') # returns (x, y) of matching region buttonx, buttony (1441, 582)
     pyautogui.click(buttonx, buttony)  # clicks the center of where the button was found
     buttonx, buttony = pyautogui.locateCenterOnScreen('button.png') # returns (x, y) of matching  buttonx, buttony (1441, 582)
     pyautogui.click(buttonx, buttony)  # clicks the center of where the button was found
    
    #SCREENSHOT_FUNCTIONS
     im1 = pyautogui.screenshot()
     im1.save('my_screenshot.png')
     im2 = pyautogui.screenshot('my_screenshot2.png')    

    #MESSAGE_FUNCTIONS
      
     pyautogui.alert('This is an alert box.')'OK'
     pyautogui.confirm('Shall I proceed?')    'Cancel'
     pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])'B' pyautogui.prompt('What is your name?') 'Al'
     pyautogui.password('Enter password (text will be hidden)')'swordfish'

"""

class ScreenObjs:
    def __init__(self):
        pass
    
    def windowCheck(self):
        title = p.getActiveWindowTitle()
        select = p.confirm(text=' A JANELA --"" {title} ""-- É A MESMA QUE RODA O JOGO?', title='== CALIBRAGEM 1 ==: A JANELA ATIVA', buttons=['SIM', 'NÃO'])
        if select == "SIM":
            p.alert("TELA CALIBRADA")
            screen = title
        elif select == "NÃO":
            select1 = p.confirm(text="POR FAVOR CLIQUE NO BOTÃO 'RECONFIGURAR' E, NA SEQUÊNCIA, CLIQUE NA JANELA QUE VAI RODAR O JOGO", title= "OPS, UM AJUSTE PRECISA SER FEITO", buttons=['RECONFIGURAR', "SAIR"])
            click = input()
            title = p.getActiveWindowTitle()
            if select1 == 'RECONFIGURAR':
                self.windowCheck()
            else:
                pass
        return title
                

#%%

"""

wds = [x.title for x  in p.getAllWindows() if x.title != ""]
for x in wds:
    p.getWindowsWithTitle(str(x)).maximize()
    t.sleep(0.5)
    p.getWindowsWithTitle(str(x)).minimize()

"""

#ESTABELECE A TELA EM DESTAQUE POR CRUZAMENTO COM O RECONHECIMENTO DE IMAGINS
#%%
#%%
#NAVIGATE
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Navigate:
    def __init__(self):
        self.ORIGIN = os.path.join("C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\IMG\\targets") 
        self.IMG_LIST= [[x,os.path.join(self.ORIGIN, x)] for x in os.listdir(self.ORIGIN)]
        #
        self.SERVER_ONLINE = ""
        #
        self.REST_ALL_BUTTON = (956,391)
        self.REST_BUTTON = ""
        #   
        self.WORK_BUTTON = ""
        self.WORK_ALL_BUTTON = (878,383)
        #
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

nv = Navigate()

so = ScreenObjs()
so.windowCheck()
#nv.keepRunning()

#ABRE A URL DO JOGO NO NAVEGADOR PADRÃO DO SISTEMA
#nv.webStart()

# %%

# %%

# %%

# %%
