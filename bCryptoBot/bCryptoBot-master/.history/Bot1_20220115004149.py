#%%

#imports

import pyautogui as p
import time
import time
from datetime import datetime
from datetime import timedelta


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
        return 
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

        
#INTERACT
# #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class Interact:
    def __init__(self):
        self.ob1_OPEN_CASE = Objects().get_OPEN_CASE(333,537)
        self.ob1_get_ALL_WORK_BT= Objects().get_ALL_WORK_BT(279,257)
        self.ob1_ALL_REST_BT = Objects().get_ALL_REST_BT(318,256)
        self.ob1_EXIT_BUTTON = Objects().get_EXIT_BUTTON(371,223)
        self.ob1_GREEN_BT = Objects().get_GREEN_BT(41,170)
        self.ob1_T_HUNT = Objects().get_T_HUNT(337,347)

        self.ob2_OPEN_CASE = Objects().get_OPEN_CASE(1017,535)
        self.ob2_ALL_WORK_BT = Objects().get_ALL_WORK_BT(961,256)
        self.ob2_ALL_REST_BT = Objects().get_ALL_REST_BT(1001,256)
        self.ob2_EXIT_BUTTON = Objects().get_EXIT_BUTTON(1055,222)
        self.ob2_GREEN_BT = Objects().get_GREEN_BT(725,169)
        self.ob2_T_HUNT = Objects().get_T_HUNT(1020,345)        

    def tempoInicial(self):
        t0 = datetime.now()
        running_time = input("Running time?...\n")
        t1 = t0 + timedelta(hours=int(running_time))
        print(f"THIS APP WILL RUN UNTIL {t1}")
    
#ESTABELECER TEMPO QUE A APLICA????O VAI RODAR

IT = Interact()
IT.tempoInicial()






