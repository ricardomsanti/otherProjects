from torch import cudnn_is_acceptable
from config  import Conf as cf
import pyautogui as p
import time as t


class Interaction:
    def __init__(self):
        self.conf = cf
        self.target = {}
        
    def getTarget(self,field=None, mode = 'click'):
        p.click(self.cf[str(field)])
        
        



        
    def refreshArena(self):
        self.getTarget(field="BC", mode='click')
        self.getTarget(field="TH", mode='click')
    
    
    def openHeroCase(self):
        
        self.getTarget('OPEN')
        self.getTarget('OPEN')
        
        
    def actionAll(self,pause_time=2, mode='WORK'):
        print("OPEN CASE")
        self.openHeroCase()
        if mode == "WORK":
            self.getTarget('D')
        elif mode == "REST":
            self.getTarget('RAO')
            
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