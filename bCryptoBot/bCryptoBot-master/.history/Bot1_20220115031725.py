#%%

#imports

import pyautogui as p
import time
import time
from datetime import datetime
from datetime import timedelta
import webbrowser as w



    


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
        

#OBJECTS
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Objects():

    def get_OPEN_CASE(self, x=None, y=None):
        OPEN_CASE  = (x,y)
        return 
    def get_ALL_WORK_BT(self, x=None, y=None):
        ALL_WORK_BT =(x,y)
        
    def get_ALL_REST_BT(self, x=None, y=None):
        ALL_REST_BT =(x,y)
        return 
    def get_EXIT_BUTTON(self, x=None, y=None):
        EXIT_BUTTON =(x,y)
        return 
    def get_GREEN_BT(self, x=None, y=None):
        GREEN_BT  = (x,y)
        return 
    def get_T_HUNT(self, x=None, y=None):
        T_HUNT  = (x,y)
        return 
    def get_IMG(self, x=None, y=None):
        T_HUNT  = (x,y)
        return 

        
#INTERACT
# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
      

#ESTABELECE POR QUANTO TEMPO A FUNCÃO VAI RODAR
def tempoInicial():
    t0 = datetime.now()
    running_time = input("Running time?...\n")
    t1 = t0 + timedelta(hours=int(running_time))
    print(f"THIS APP WILL RUN UNTIL {t1}")
    

#ABRE A URL DO JOGO NO NAVEGADOR PADRÃO DO SISTEMA
 
def webStart(self):
    w = w.WindowsDefault()
    url = "https://bombcrypto.io/"
    w.open(self.url)


#ESTABELECER TEMPO QUE A APLICAÇÃO VAI RODAR
tempoInicial()

webStart()





