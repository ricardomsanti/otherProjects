from torch import cudnn_is_acceptable
from config.py import Conf as cf
import pyautogui as p
import time as t


class Interaction:
    def __init__(self):
        self.conf = cf
        
    
    def getTarget(self,field=None, mode = 'click'):
        
        #entra NOME e sai coordenada
        
  
        
        T_HUNT_CDR = ""
        REST_BUTTON_ROOT_CDR = ""
        EXIT_BT_CDR = (1041, 264)
        T_BACK_BUTTON_CDR = (533, 174)
        REST_ALL_BUTTON_CDR = (952, 305)
        T_OPEN_HERO_CASE_BUTTON_CDR = (972, 717)
        WORK_ALL_BUTTON_CDR = (890, 306)
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
        print(str(field))
        p.cllck(target[str(field)])
        t.sleep(2)
        return               
        
    def refreshArena(self):
        self.getTarget(field="T_BACK_BUTTON_CDR", mode='click')
        self.getTarget(field="T_HUNT_CDR", mode='click')
    
    
    def openHeroCase(self):
        
        self.getTarget('T_OPEN_HERO_CASE_BUTTON_CDR')
        self.getTarget('T_OPEN_HERO_CASE_BUTTON_CDR')
        
        
    def actionAll(self,pause_time=2, mode='WORK'):
        
        self.openHeroCase
        if mode == "WORK":
            self.getTarget('WORK_ALL_BUTTON_CDR')
        elif mode == "REST":
            self.getTarget('REST_ALL_BUTTON_CDR')
            
        self.getTarget('EXIT_BT_CDR')
        self.getTarget('EXIT_BT_CDR')
  
    
    def keepRunning(self, limit = 0,t1=0, t2=0):
        
        #alternar as rotinas worlall e rest all por um determinado tempo
        
        print("INICIANDO SEQUÊNCIA\n")
        counter = 0
        while limit > counter:
            
            self.actionAll(self.actionAll(mode="work"))
            t.sleep(t1)
            self.actionAll(self.actionAll(mode="rest"))
            t.sleep(t2)
            counter += 1
            if counter > limit:
                print("SEQUENCIA FINALIZADA")
                break
