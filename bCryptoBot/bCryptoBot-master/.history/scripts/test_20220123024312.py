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


while True:
    m = win32gui.GetCursorPos()

    rect = win32gui.CreateRoundRectRgn(*past_coordinates, 2 , 2)
    win32gui.RedrawWindow(hwnd, past_coordinates, rect, win32con.RDW_INVALIDATE)

    for x in range(10,100,10):
        win32gui.SetPixel(dc, m[0]+x, m[1], green)
        win32gui.SetPixel(dc, m[0], m[1]+x, green)
     #   for y in range(10):

    #past_coordinates = (m[0]-20, m[1]-20, m[0]+20, m[1]+20)
