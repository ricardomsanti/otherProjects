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
from Interact import Interaction    
from config import Conf as cf

########################################################################

bigScreenCoord = {
    'TH':    (997, 493 ),    
    'BC':    (539, 186 ),    
    'OPEN':  (971, 732 ),
    'OA':    (899, 322 ),    
    'RA':    (952, 323 ),   
    'RO':    (948, 362 ),    
    'WO':    (889, 368 ),    
    'H':    (662, 361) }

########################################################################

it = Interaction()

#it.keepRunning(10)
while 1:
    it.getTarget('OPEN')
    t.sleep(2)
