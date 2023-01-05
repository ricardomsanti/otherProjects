
#%%

import os
from PIL import Image
import pyautogui as p
import win32gui, win32ui, win32api, win32con
from win32api import GetSystemMetrics



####
# HÁ TRÊS FORMAS DE SE LOCALIZAR UM PONTO NA TELA
#  -- BUSCA POR IMAGENS
#  -- BUSCA POR COORDENADAS
#  -- DEDUÇÃO DE COORDENADAS 
#
#

###
class Locator:
    def __init__(self):
        self.reference_fodlder = os.getcwd()
        self.IMG_FILES = [ x for x in os.listdir(self.reference_fodlder) if ".png" in x]

    def loadImgs(self):
        for x in self.reference_files:
                
          return self.IMG_REF    

      
    


lc = Locator()

lc.getReference()