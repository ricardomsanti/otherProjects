#%%
from traceback import print_list
import pyautogui as p
import time as t
from datetime import datetime
from datetime import timedelta
import webbrowser as w
import pandas as pd
import random as r
import os
import pyautogui as p
import time as t
from datetime import datetime
from datetime import timedelta
import webbrowser as w
import pandas as pd
import os
import pyautogui as p
        
t.sleep(10)


if  p.getActiveWindowTitle == "Bombcrypto - Opera":
    
    from Interact import Interaction
    it.keepRunning(limit=3,t1=3,t2=5)


'''

def windowSelect():

    wds = [p.getWindowsWithTitle(x) for x in p.getAllTitles() if p.getWindowsWithTitle(x) != ""]
    for x in wds:
        
    #current_window = p.getWindowsWithTitle(mainTitle)
    for x in range(10):
        x, y =  p.getActiveWindow()
        mainTitle = p.getActiveWindow()
        mainTitle.resize(x - 10, y -10)
        active.resize(x , y)
'''