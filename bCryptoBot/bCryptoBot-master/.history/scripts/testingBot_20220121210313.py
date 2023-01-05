#%%
import pyautogui as p
i= ""
pos_list = []
while i == "":
    confirm = input("Marcar novo ponto?")
    if confirm=="s":
        COORD = p.position()
        pos_list.append(COORD)
    elif confirm == "n":
        i= "end"
    else:
        continue
print(pos_list)