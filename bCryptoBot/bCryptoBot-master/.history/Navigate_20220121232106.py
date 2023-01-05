

class Navigate:
    def __init__(self):
        pass
    
    def tempoInicial(self):
        t0 = datetime.now()
        running_time = input("Running time?...\n")
        t1 = t0 + timedelta(hours=int(running_time))
        print(f"THIS APP WILL RUN UNTIL {t1}")
        
  
        
    def webStart(self):
        url = "https://bombcrypto.io/"
        w.WindowsDefault(url)