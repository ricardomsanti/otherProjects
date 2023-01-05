#%%
from tkinter.ttk import Button
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
from Interact import Interaction as it      

t.sleep(10)





def windowCheck():
    i = input()
    p.click()
    w = p.getActiveWindow()
    print(w.name)
        
windowCheck()