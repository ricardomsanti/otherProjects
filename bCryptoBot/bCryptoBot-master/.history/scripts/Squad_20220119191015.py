import pandas as pd
from . import Hero as h
h = h.Hero()

class Squad:
    def __init__(self):
        self.hero_squad = []
        self.squad_owner = []
    def load_squad(self):
        DATA_REF_FILE = "C:\\Users\\QQ\\Google Drive\\CODE_DRIVE\\CRYPTO\\FINAL_REFERENCE.xlsx"     
        DATA_REF = pd.read_excel(DATA_REF_FILE)
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
        
  
    def warBus(self, sqaud=None, ruleLists = None):