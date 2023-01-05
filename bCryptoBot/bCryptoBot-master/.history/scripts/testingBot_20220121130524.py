#%%

import time as t

def busDriver():
    while 1:
        print("Bus driver!")
        t.sleep(2)
import pygame as pg

import pyautogui as p

act = p.getActiveWindow()
pg.draw.rect()
pg.draw.rect(act,(23,232,232),width=30)