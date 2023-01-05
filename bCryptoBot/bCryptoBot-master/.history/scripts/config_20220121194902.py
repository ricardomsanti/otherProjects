import os

class Conf:
    def __init__(self):        
        self.BLUE_BOX = 'BLUE_BOX'
        self.BROWN_BOX = 'BROWN_BOX'
        self.PURPLE_BOX = 'PURPLE_BOX'
        self.YELLOW_BOX = 'YELLOW_BOX'
        self.T_HUNT = 'T_HUNT'
        self.REST_BUTTON_ROOT = 'REST_BUTTON_ROOT'
        self.EXIT_BT = 'EXIT_BT'
        self.T_BACK_BUTTON = 'T_BACK_BUTTON'
        self.REST_ALL_BUTTON = 'REST_ALL_BUTTON'
        self.T_OPEN_HERO_CASE_BUTTON = 'T_OPEN_HERO_CASE_BUTTON'
        self.WORK_ALL_BUTTON = 'WORK_ALL_BUTTON'
        self.WORK_BUTTON_ROOT = 'WORK_BUTTON_ROOT'
        self.BLUE_BOX_CDR = (0,0),                    	                   
        self.BROWN_BOX_CDR = (0,0),                    	                   
        self.PURPLE_BOX_CDR = (0,0),              
        self.YELLOW_BOX_CDR = (0,0),                                          
        self.T_HUNT_CDR = (960, 4),              
        self.REST_BUTTON_ROOT_CDR = (675,301),     
        self.EXIT_BT_CDR =  (732,301),
        self.T_BACK_BUTTON_CDR = (345,174),   	                      
        self.REST_ALL_BUTTON_CDR = (676,282),      
        self.T_OPEN_HERO_CASE_BUTTON_CDR = (694,606),                     
        self.WORK_ALL_BUTTON_CDR = (632,276),                     
        self.WORK_BUTTON_ROOT_CDR = (632,306)
        self.BLUE_BOX_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'blue_box.png')
        self.BROWN_BOX_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'brown_box.png')
        self.PURPLE_BOX_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'purple_box.png')
        self.YELLOW_BOX_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'yellow_box.png')
        self.REST_ALL_BUTTON_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'REST_ALL_BUTTON.png')
        self.REST_BUTTON_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'REST_BUTTON.png')
        self.SERVER_ONLINE_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'SERVER_ONLINE.png')
        self.TRASH_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'TRASH.png')
        self.T_B_BUTTON_LEFT_IMG = os.path.join(os.getcwd(),'IMG//targets' ,'T_B_BUTTON_LEFT.png')
        self.T_HUNT_IMG =  os.path.join(os.getcwd(),'IMG//targets' ,'T_HUNT.png')
        self.T_OPEN_HERO_CASE_BUTTON_IMG =  os.path.join(os.getcwd(),'IMG//targets' ,'T_OPEN_HERO_CASE_BUTTON.png')
        self.T_START_GAME_IMG =  os.path.join(os.getcwd(),'IMG//targets' ,'T_START_GAME.png')
        self.WORK_ALL_BUTTON_IMG =  os.path.join(os.getcwd(),'IMG//targets' ,'WORK_ALL_BUTTON.png')
        self.WORK_BUTTON_IMG=  os.path.join(os.getcwd(),'IMG//targets' ,'WORK_BUTTON.png')
            
        
        
import pyautogui as p
C = Conf()
p.locateOnScreen(C.T_HUNT_IMG) 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    


