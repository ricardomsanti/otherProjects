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








def windowCheck():
    for x in p.getAllWindows():
        msg = p.confirm(text="POR FAVOR SELECTIONE A JANELA ONDE SERÁ EXECUTADO O PROGRAMA",title='CONFIG', buttons=[ str(x.name()) , 'PRÓXIMA'])
        msg.add()
    print(w)
        
windowCheck()