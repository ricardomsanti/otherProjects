#%%

#imports

import pyautogui as p
import time
import time
from datetime import datetime
from datetime import timedelta
import webbrowser as w
import pandas as pd
import random as r
import os.path

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


#%%








