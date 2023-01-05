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
        ob1 = Objects()
        ob2 = Objects()
        ob1_OPEN_CASE = ob1.get_OPEN_CASE(333,537)
        ob1_get_ALL_WORK_BT= ob1.get_ALL_WORK_BT(279,257)
        ob1_ALL_REST_BT = ob1.get_ALL_REST_BT(318,256)
        ob1_EXIT_BUTTON = ob1.get_EXIT_BUTTON(371,223)
        ob1_GREEN_BT = ob1.get_GREEN_BT(41,170)
        ob1_T_HUNT = ob1.get_T_HUNT(337,347)

        ob2_OPEN_CASE = ob2.get_OPEN_CASE(1017,535)
        ob2_ALL_WORK_BT = ob2.get_ALL_WORK_BT(961,256)
        ob2_ALL_REST_BT = ob2.get_ALL_REST_BT(1001,256)
        ob2_EXIT_BUTTON = ob2.get_EXIT_BUTTON(1055,222)
        ob2_GREEN_BT = ob2.get_GREEN_BT(725,169)
        ob2_T_HUNT = ob2.get_T_HUNT(1020,345)
        

    def tempoInicial(self):
        t0 = datetime.now()
        running_time = input("Running time?...\n")
        t1 = t0 + timedelta(hours=int(running_time))
        print(f"THIS APP WILL RUN UNTIL {t1}")
    
#ESTABELECER TEMPO QUE A APLICAÇÃO VAI RODAR

IT = Interact()
IT.tempoInicial()






