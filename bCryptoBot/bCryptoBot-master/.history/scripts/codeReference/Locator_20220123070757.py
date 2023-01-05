import os
from PIL import Image
import pyautogui as p
import win32gui, win32ui, win32api, win32con

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

        
    def getReference(self, mode='list', item=None):
        
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
    
   
from win32api import GetSystemMetrics

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

    for x in range(10):
        win32gui.SetPixel(dc, m[0]+x, m[1], green)
        win32gui.SetPixel(dc, m[0]+x, m[1]+10, green)
        for y in range(10):
            win32gui.SetPixel(dc, m[0], m[1]+y, green)
            win32gui.SetPixel(dc, m[0]+10, m[1]+y, green)

    past_coordinates = (m[0]-20, m[1]-20, m[0]+20, m[1]+20)
    
lc = Locator()
    def findTopHero(self):
        
569,386
568,676
564,731
1052,734