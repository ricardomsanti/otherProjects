#%%

#imports
import pyautogui as p
import time as t
from datetime import datetime
from datetime import timedelta
import webbrowser as w
import pandas as pd
import random as r
from . import navigate, hero, screenobjs, squad



nv = Navigate()

#LOAD_SQUAD
sq = Squad()
sq.load_squad()
R_SQUAD = [x for x in sq.hero_squad if x.Conta[0] == "Ricardo"]
print(R_SQUAD[1])

p.displayMousePosition()
# p.displayMousePosition()

f_head = (200,2333)
          
