#%%
import pyautogui as p
i= ""
pos_list = []
while i == "":
    confirm = input("Marcar novo ponto?")
    if confirm=="s":
        COORD = p.position()
        NAME = input("Nome da referência:")
        pos_list.append([COORD,NAME])
    elif confirm == "n":
        i= "end"
    else:
        continue
print(pos_list)