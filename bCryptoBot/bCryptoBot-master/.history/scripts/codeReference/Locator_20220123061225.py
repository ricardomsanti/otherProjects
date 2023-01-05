import os
from PIL import Image
import pyautogui as p

class Locator:
    def __init__(self):
        self.reference_fodlder = os.path.join(os.getcwd(),"IMG\\targets")
        self.recerence_files = [ x for x in os.listdir(self.reference_fodlder)]
        self.IMG_REF = {}
    def loadImgs(self):
        for x in self.recerence_files:
            self.IMG_REF.update = {"filename": str(x),
                              "file" : Image.open(os.path.join(os.getcwd(),"IMG\\targets",x)),
                              "coordenates": p.locateOnScreen(Image.open(os.path.join(os.getcwd(),"IMG\\targets",x)))
                                }
lc = Locator()