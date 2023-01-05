import pyautogui 
import time
from datetime import datetime

print(datetime.datetime.now())

cl = input("Press Enter for clicl")
for x in range(3):
    print(x)
    time.sleep(1)
B_BUTTON_LEFT = (325,164)
pyautogui.click(B_BUTTON_LEFT)