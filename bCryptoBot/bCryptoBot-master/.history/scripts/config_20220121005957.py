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
        
        
        
        def getCrd(self, so=None):
            
            crdDict = {
                'BLUE_BOX' : (0,0),                    	                   
                'BROWN_BOX' : (0,0),                    	                   
                'PURPLE_BOX' : (0,0),              
                'YELLOW_BOX' : (0,0),                                          
                'T_HUNT' : (960, 4),              
                'REST_BUTTON_ROOT' : (675,301),     
                'EXIT_BT' :  (732,301),
                'T_BACK_BUTTON' : (345,174),   	                      
                'REST_ALL_BUTTON' : (676,282),      
                'T_OPEN_HERO_CASE_BUTTON' : (694,606),                     
                'WORK_ALL_BUTTON' : (632,276),                     
                'WORK_BUTTON_ROOT' : (632,306)
                                                }     
            
            return = crdDict[so]
        
        
        def getImg(self, so=None):
            imglist = []
            imgList = [ [BLUE_BOX ],[ os.path.join(os.getcwd(), 'blue_box.png')],
                [BROWN_BOX ],[ os.path.join(os.getcwd(), 'brown_box.png')],
                [PURPLE_BOX ],[ os.path.join(os.getcwd(), 'purple_box.png')],
                [YELLOW_BOX ],[ os.path.join(os.getcwd(), 'yellow_box.png')],
                [REST_ALL_BUTTON ],[ os.path.join(os.getcwd(), 'REST_ALL_BUTTON.png')],
                [REST_BUTTON ],[ os.path.join(os.getcwd(), 'REST_BUTTON.png')],
                [SERVER_ONLINE ],[ os.path.join(os.getcwd(), 'SERVER_ONLINE.png')],
                [TRASH ],[ os.path.join(os.getcwd(), 'TRASH.png')],
                [T_B_BUTTON_LEFT ],[ [os.path.join(os.getcwd(), 'T_B_BUTTON_LEFT.png')],
                [T_HUNT ],[  os.path.join(os.getcwd(), 'T_HUNT.png')],
                [T_OPEN_HERO_CASE_BUTTON ],[  os.path.join(os.getcwd(), 'T_OPEN_HERO_CASE_BUTTON.png')],
                [T_START_GAME ],[  os.path.join(os.getcwd(), 'T_START_GAME.png')],
                [WORK_ALL_BUTTON ],[  os.path.join(os.getcwd(), 'WORK_ALL_BUTTON.png')],
                [WORK_BUTTON ],[  os.path.join(os.getcwd(), 'WORK_BUTTON.png')]
            ]
            result = [x for x in imglist if x[0] == so]
            result = imgRef[so]
        
        
        def getByCoord():
            
        
        self.COORD_BLUE_BOX, 
        self.COORD_BROWN_BOX, 
        self.COORD_PURPLE_BOX, 
        self.COORD_YELLOW_BOX, 
        self.COORD_T_HUNT, IMG_T_HUNT])    
        self.COORD_REST_BUTTON_ROOT, ""])    
        self.COORD_EXIT_BT, ""])    
        self.COORD_T_BACK_BUTTON, ""])    
        self.COORD_REST_ALL_BUTTON, IMG_REST_ALL_BUTTON])    
        self.COORD_T_OPEN_HERO_CASE_BUTTON, IMG_T_OPEN_HERO_CASE_BUTTON])    
        self.COORD_WORK_ALL_BUTTON, IMG_WORK_ALL_BUTTON])    
        self.COORD_WORK_BUTTON_ROOT, ""])            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    


