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
    p.alert("POR FAVOR CLIQUE NO BOTÃO ABAIXO E, NA SEQUÊNCIA, CLIQUE SOBRE ALGUMA ÁREA VAZIA DA JANELA\n"
            "ONDE O JOGO VAI A ACONTERCER")

    w = p.getActiveWindow()
    print(w)
        
windowCheck()