import pandas as pd

class Squad:
    def __init__(self, source_file = None, owner_name=None, tab_name=None):
        self.source_file = source_file
        self.owner_name = owner_name  
        self.hero_squad = []
        self.squad_owner = []
        self.tab_name = tab_name
        
    def heroBox(self):
        box_height_max = (568,676)
        box_height_min1 =(568,731) 
        box_height_min2 =(1052,731)
        
        



    def load_squad(self):        
        DATA_REF = pd.read_excel(self.source_file,sheet_name=self.tab_name)
        for index, row in DATA_REF.iterrows():
            h = Hero(\
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
            self.hero_squad.append(h)
  