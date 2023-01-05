#%%
import pyautogui as p
i= ""
pos_list = []
while i == "":
    confirm = input("Marcar novo ponto?")
    if confirm:
        COORD = p.position
        pos_list.append(COORD)
    else:
        i= "end"
print(pos_list)