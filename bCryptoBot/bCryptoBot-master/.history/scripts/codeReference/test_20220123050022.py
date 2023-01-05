
#%%import pyautogui as p
import win32gui, win32ui, win32api, win32con
from win32api import GetSystemMetrics
import pyautogui as p
from PIL import Image



dc = win32gui.GetDC(0)
dcObj = win32ui.CreateDCFromHandle(dc)
hwnd = win32gui.WindowFromPoint((0,0))
monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))
green = win32api.RGB(0,255, 0)

past_coordinates = monitor
rect = win32gui.CreateRoundRectRgn(*past_coordinates, 2 , 2)
win32gui.RedrawWindow(hwnd, past_coordinates, rect, win32con.RDW_INVALIDATE)

past_coordinates = monitor

BC = Image.open('C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\bCryptoBot\\scripts\\codeReference\\IMG\\targets\\BC.png') 

while 1:
    
    center_cursor = win32gui.GetCursorPos()
    locate = (p.locateOnScreen(BC))
    rect = win32gui.CreateRoundRectRgn(*past_coordinates, 2 , 2)
    win32gui.RedrawWindow(hwnd, past_coordinates, rect, win32con.RDW_INVALIDATE)

    for x in range(1,200,2):
        resize = 60
        rx, ry  = (center_cursor[0] , center_cursor[1])
        
        win32gui.SetPixel(dc, rx + x, ry, green)
        win32gui.SetPixel(dc, rx -x, ry, green)
        win32gui.SetPixel(dc, rx, ry + x, green)
        win32gui.SetPixel(dc, rx, ry - x, green)
    past_coordinates = (rx-int(resize), ry-int(resize), rx+int(resize), ry+int(resize))
    if locate != None:
        break
        print(p.locateOnScreen(BC))