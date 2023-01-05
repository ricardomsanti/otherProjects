#%%
import os
from datetime import datetime as dt
from datetime import timedelta as td
import pyautogui as p
class Conf:
    def __init__(self,SCREEN_REF={}):        
        self.BLUE_BOX = 'BLUE_BOX',
        self.BROWN_BOX = 'BROWN_BOX',
        self.PURPLE_BOX = 'PURPLE_BOX',
        self.YELLOW_BOX = 'YELLOW_BOX',
        self.TH = 'TH',
        self.RO = 'RO',
        self.EXIT_BT = 'EXIT_BT',
        self.BC = 'BC',
        self.RA = 'RA',
        self.OPEN = 'OPEN',
        self.WA = 'WA',
        self.WO = 'WO',
        self.SCREEN_REF = SCREEN_REF,
        ###############################################IMG
        self.BLUE_BOX_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'blue_box.png')
        self.BROWN_BOX_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'brown_box.png')
        self.PURPLE_BOX_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'purple_box.png')
        self.YELLOW_BOX_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'yellow_box.png')
        self.RA_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'RA.png')
        self.REST_BUTTON_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'REST_BUTTON.png')
        self.SERVER_ONLINE_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'SERVER_ONLINE.png')
        self.TRASH_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'TRASH.png')
        self.T_B_BUTTON_LEFT_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'T_B_BUTTON_LEFT.png')
        self.TH_IMG =  os.path.join(os.getcwd(),'IMG//targets' ,'TH.png')
        self.OPEN_IMG =  os.path.join(os.getcwd(),'IMG//targets' ,'OPEN.png')
        self.T_START_GAME_IMG =  os.path.join(os.getcwd(),'IMG//targets' ,'T_START_GAME.png')
        self.WA_IMG =  os.path.join(os.getcwd(),'IMG//targets' ,'WA.png')
        self.WORK_BUTTON_IMG=  os.path.join(os.getcwd(),'IMG//targets' ,'WORK_BUTTON.png')
        
    

    def windowCheck(self):
        p.alert("Window Check")
        wds = [x.name for x in p.getAllTitles()]
        for x in wds:
            selection = p.confirm(text="POR FAVOR SELECTIONE A JANELA ONDE SERÁ EXECUTADO O PROGRAMA",title='CONFIG', buttons=[ str(x) , 'PRÓXIMA'])
            if selection != "PROXIMA":
                result = selection
            else:
                continue
        return result


    def objReference(self):
        for x in 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    


