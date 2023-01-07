import pywhatkit as w
from datetime import datetime as dt
from progress.bar import IncrementalBar
import time

"""number = input("Send to:\n")
times = input("How many times?\n")
message = input("Message: \n")
"""
number = "+55 24 98148-8822"
times = 50
message = "olá humana"
bar = IncrementalBar("dsds".)

select = ""
while select == "":
    hour = dt.now().hour
    sec = dt.now().second
    min = dt.now().minute
    w.sendwhatmsg(phone_no=number,message=message,time_hour=hour, time_min=min+1, wait_time=0,print_waitTime=True)
    select = input(sec)


w.text_to_handwriting("jdnfjdnfldfn","snndskdd.png",[0,0,0])