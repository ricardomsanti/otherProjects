import pandas as pd
from . import Hero as h
import os
h = h.Hero()

  

class Squad:
    def __init__(self, source_file = None, owner_name=None, tab_name=None):
        self.source_file = source_file
        self.owner_name = owner_name  
        self.hero_squad = []
        self.squad_owner = []
        self.tab_name = tab_name
    def load_squad(self, sourceFile = None):
        DATA_REF = pd.read_excel(self.source_file,sheet_name=self.tab_name)
        for index, row in DATA_REF.iterrows():
            hr = h(\
                    row['Conta'],\
                    row['ID'],\
                    row['Vida'],\
                    row['Power'],\
                    row['Speed'],\
                    row['Stamina'],\
                    row['Bomb Numb'],\
                    row['Bomb Range'],\
                    row['Extra 1'],\
                    row['Extra 2'],\
                    row['Extra 3'],\
                    row['Extra 4'],\
                    row['Extra 5'],\
                    row['CHARGE_CHECK'],\
                    row['TIPO_COMUM'],\
                    row['REC/H'],\
                    row['TOTAL_MIN'],\
                    row['TOTAL_HORA'])
            self.hero_squad.append(hr)
        
"""
    def warBus(self, sqaud=None, ruleLists = None):
        pass

"""