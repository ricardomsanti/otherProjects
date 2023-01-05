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

        
t.seel(10)
if  p.getActiveWindowTitle == "Bombcrypto - Opera":
    
    from Interact import Interaction
    it = Interaction()
    it.keepRunning(limit=3,t1=3,t2=5)
