#%%


#imports
import pyautogui as p
import time as t
from datetime import datetime
from datetime import timedelta
import webbrowser as w
import pandas as pd
import random as r
import Navigate as n
import Hero  as h
#import Objs  as s
import Squad as sq



SQUAD_SOURCE_FILE = "C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\FINAL_REFERENCE.xlsx"   


#LOAD_SQUAD
squad = sq.load_squad(source_file=SQUAD_SOURCE_FILE,owner_name="Ricardo",tab_name='TARGET_REFERENCE' )
print(squad)


