from torch import cudnn_is_acceptable
from scripts.config import Conf as cf
import pyautogui as p
import time as t


class Interaction:
    def __init__(self):
        self.conf = cf
        
        
        
    
    def getTarget(field=None, mode = 'click'):
        
        #entra NOME e sai coordenada
        
        T_HUNT_CDR = ""
        REST_BUTTON_ROOT_CDR = ""
        EXIT_BT_CDR = ""
        T_BACK_BUTTON_CDR = ""
        REST_ALL_BUTTON_CDR = ""
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
  
    
    def keepRunning(self):
        
        #alternar as rotinas worlall e rest all por um determinado tempo
        
        print("INICIANDO SEQUÊNCIA\n")
        
        t.sleep(2)
        pause_time = 2
        waitForNext = 2
        delta = 0
        x = 1
        #RODAR INDEFINIDAMENTE
        t0 = datetime.now()
        while x == 1:
            t1 = datetime.now()
            print(f"TEMPO INICIAL IGUAL A {t1}")
            delta = t1 - t0
            #RODAT ATÉ QUE
            if delta.seconds < 25:
                print("ATIVAÇÃO EM PROGRESSO")
                self.workAll(pause_time=pause_time)
                print("PAUSA")
                self.refreshArena()
                print("RENOVAÇÃO_PÁGINA")
                t.sleep(waitForNext)
                self.refreshArena()
                print("PAUSA")
                t.sleep(waitForNext)
                print("DESATIVAÇÃO EM PROGRESSO")
                self.restAll(pause_time=pause_time)
                self.refreshArena()
                t.sleep(waitForNext)
                self.refreshArena()
                t.sleep(waitForNext)
                self.refreshArena()
                t.sleep(waitForNext)
                t1 = datetime.now()
                delta = t1 - t0
                #REALIZADA A CONDICAO
            elif delta.seconds > 25*60:
                break
        

    def     
Clicar no botão verde e clicar em Treasure Hunt
Se tiver só 1 baú no mapa, verificar quantos espaços tem para deixar bomba (2, 3 ou 4) e desligar o restante dos bonecos. Manter apenas os que estiverem com maior vida e que tenham menos velocidade (opcional)
Quando começar um mapa novo, voltar à estratégia inicial, ligando os bonecos normalmente
Abrir a bandeja e escanear o ID do boneco para verificar se é ele que deve ser ligado/desligado, caso não, descer e verificar o debaixo, até chegar no correto
Abrir a bandeja e escanear o ID do boneco para verificar se a vida dele está cheia ou perto de, caso não, descer e verificar o debaixo. Se não houver nenhum, não executar nenhuma ação


if serhumano
    if homem
        if trans
        elif
        if cis
            if rico else
            else
        else



else


