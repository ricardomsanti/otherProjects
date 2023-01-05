from torch import cudnn_is_acceptable
from config  import Conf as cf
import pyautogui as p
import time as t


class Interaction:
    def __init__(self):
        self.conf = cf
        
    
    def getTarget(self,field=None, mode = 'click'):
        
        
        T_HUNT_CDR = ""
        REST_BUTTON_ROOT_CDR = ""
        EXIT_BT_CDR =""
        T_BACK_BUTTON_CDR =  ""
        REST_ALL_BUTTON_CDR =""
        T_OPEN_HERO_CASE_BUTTON_CDR = "" 
        WORK_ALL_BUTTON_CDR = ""
        WORK_BUTTON_ROOT_CDR = ""
        
        
        target = {
            "T_HUNT_CDR": T_HUNT_CDR,
            "REST_BUTTON_ROOT_CDR": REST_BUTTON_ROOT_CDR,
            "EXIT_BT_CDR": EXIT_BT_CDR,
            "T_BACK_BUTTON_CDR": T_BACK_BUTTON_CDR,
            "REST_ALL_BUTTON_CDR": REST_ALL_BUTTON_CDR,
            "T_OPEN_HERO_CASE_BUTTON_CDR": T_OPEN_HERO_CASE_BUTTON_CDR,
            "WORK_ALL_BUTTON_CDR": WORK_ALL_BUTTON_CDR,
            "WORK_BUTTON_ROOT_CDR": WORK_BUTTON_ROOT_CDR
        }                   
        
        for x, y in target.items():
            
        
            selection = p.confirm(text="POR FAVOR ENCONTRE O ITEM QUE DESEJA RECALIBRAR, CLIQUE NO BOTÃO RECLIBRAR E, DURANTE OS PRÓXIMOS 5 SEGUNDOS \t"
                                  "DEIXE O CURSOR SOBRE O CENTRO DO ALVO",title=f'RECALIBRAR : str(x)', buttons=[ str(x) , 'PRÓXIMA'])
        if selection != "PROXIMA":
            result = selection
        else:
            pass
        return result

            
        print(str(field))
        p.click(target[str(field)])
        t.sleep(2)
        return               
        
    def refreshArena(self):
        self.getTarget(field="T_BACK_BUTTON_CDR", mode='click')
        self.getTarget(field="T_HUNT_CDR", mode='click')
    
    
    def openHeroCase(self):
        
        self.getTarget('T_OPEN_HERO_CASE_BUTTON_CDR')
        self.getTarget('T_OPEN_HERO_CASE_BUTTON_CDR')
        
        
    def actionAll(self,pause_time=2, mode='WORK'):
        print("OPEN CASE")
        self.openHeroCase()
        if mode == "WORK":
            self.getTarget('WORK_ALL_BUTTON_CDR')
        elif mode == "REST":
            self.getTarget('REST_ALL_BUTTON_CDR')
            
        self.getTarget('EXIT_BT_CDR')
        self.getTarget('EXIT_BT_CDR')
  
    
    def keepRunning(self, limit = 5,t1=1, t2=3):
        
        #alternar as rotinas worlall e rest all por um determinado tempo
        
        print("INICIANDO SEQUÊNCIA\n")
        counter = 0
        while limit > counter:
            
            self.actionAll(pause_time=2,mode="WORK")
            t.sleep(t1)
            self.actionAll(self.actionAll(pause_time=2,mode="REST"))
            t.sleep(t2)
            counter += 1
            if counter > limit:
                print("SEQUENCIA FINALIZADA")
                break

    def checkRef(self):
        i= ""
        pos_list = []
        while i == "":
            confirm = input("Marcar novo ponto?")
            if confirm=="s":
                COORD = p.position()
                NAME = input("Nome da referência:")
                pos_list.append([COORD,NAME])
            elif confirm == "n":
                i= "end"
            else:
                continue
        print(pos_list)