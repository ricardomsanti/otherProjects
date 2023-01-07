from win10toast import ToastNotifier
from datetime import datetime as dt
from datetime import timedelta as td


#Initialyze

t = ToastNotifier()



delta = td(seconds=5)          
check = ""
while check == "":
    now = dt.now()
    t.show_toast(title="Essa é a hora atual do sistema",
                msg="Agora são {} hrs ".format(str(dt.now())),
                threaded=True,
                duration=4)
    check = input("New value?")
"""
    print("This is {}".format(now))
    t1 = now 
    print("This is t1{}".format(t1))
    t2 = t1 + delta
    print("This is t2{}".format(t2))"""
    
