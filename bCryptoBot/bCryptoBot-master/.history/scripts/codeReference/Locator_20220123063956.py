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
            self.IMG_REF[ str(x)] = {  "file" : Image.open(os.path.join(os.getcwd(),"IMG\\targets",x)),
                              "coordenates": p.locateOnScreen(Image.open(os.path.join(os.getcwd(),"IMG\\targets",x)))
                                }

        
    def referenceList(self, mode='list', item=None):
        
        if mode == 'list':
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
        else :
            pos_item = []
            while i == "":
                confirm = input("Digite s e pressione entender após deixar o mouse exatamente sobre o ponto solicitado")
                if confirm=="s":
                    COORD = p.position()
                    pos_item = [item, COORD]
                    i= "end"
        return pos_list
    
    
    
lc = Locator()
    def findTopHero(self):
        
569,386
568,676
564,731
1052,734