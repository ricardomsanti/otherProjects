#%%
import os
from cv2 import DFT_REAL_OUTPUT
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

import pyautogui as p


ORIGIN_IMG_PATH = "C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\IMG\\targets"
IMGS = [os.path.join(ORIGIN_IMG_PATH, x) for x in os.listdir(ORIGIN_IMG_PATH)]
IMGS

import pandas as pd

df = pd.DataFrame(IMGS)

#%%
x = 'a'
while x != "b":
    #for x in IMGS:
        #print("rodou completo")
    total = len(list((p.locateAllOnScreen(IMGS[2])))) 
    if total != 0:
        print(f"ae caralho, tem encontrei, da uma olhada")
        print(p.locateAllOnScreen(IMGS[2]))
    else:
        print("to achando esse porra não")