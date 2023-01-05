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

        
t.sleep(10)
if  p.getActiveWindowTitle == "Bombcrypto - Opera":
    
    from Interact import Interaction
    it.keepRunning(limit=3,t1=3,t2=5)



#%%
url = "https://bombcrypto.io/"
w.WindowsDefault(url)
#%%
import pyautogui as p
mainTitle = [x for x in p.getAllTitles()]
for x in mainTitle:
    current_window = p.getWindowsWithTitle(mainTitle)
    for x in range(10):
        x, y =  p.getActiveWindow()
        active = p.getActiveWindow()
        active.resize(x - 10, y -10)
        active.resize(x , y)


