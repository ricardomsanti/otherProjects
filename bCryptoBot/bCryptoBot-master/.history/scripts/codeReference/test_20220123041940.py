
#%%import pyautogui as p
import win32gui, win32ui, win32api, win32con
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

while 1:

    pos_cursor = win32gui.GetCursorPos()

    rect = win32gui.CreateRoundRectRgn(*past_coordinates, 2 , 2)
    win32gui.RedrawWindow(hwnd, past_coordinates, rect, win32con.RDW_INVALIDATE)

    for x in range(1,500,10):
        rx, ry  = (pos_cursor[0] + x, pos_cursor[1] +x)
        win32gui.SetPixel(dc, rx, ry, green)
        #rx, ry  = (pos_cursor[0], pos_cursor[1] + x)
        #win32gui.SetPixel(dc, rx, ry, green)
        #rx, ry  = (pos_cursor[0]-x, pos_cursor[1] + x)
        #win32gui.SetPixel(dc, rx, ry, green)
        #rx, ry  = (pos_cursor[0], pos_cursor[1] -y )
        #win32gui.SetPixel(dc, rx, ry, green)
        
        #win32gui.SetPixel(dc, pos_cursor[0], pos_cursor[1], green)
        #win32gui.SetPixel(dc, pos_cursor[0]+x, pos_cursor[1]+x, green)
        #win32gui.SetPixel(dc, pos_cursor[0], pos_cursor[1], green)
        #win32gui.SetPixel(dc, pos_cursor[0]+10, pos_cursor[1]+y, green)
#%%