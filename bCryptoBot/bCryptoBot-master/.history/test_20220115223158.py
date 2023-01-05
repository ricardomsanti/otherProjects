range = ""
#%%

def n_p(range=None):
    div_zero = [x for x in range() if int(x)%0 == 1]
    print(div_zero)
n_p(100)




#%%

print("SEM FILTROS\n")
div_zero = [x for x in range(1,100)]
print(f"LISTA TOTAL: {div_zero}")
print(f"TOTAL: {len(div_zero)}")
print("VALORES PARES")
print()
div_zero = [x for x in range(1,100) if x%2 ==0]
print(f"LISTA TOTAL: {div_zero}")
print(f"TOTAL: {len(div_zero)}")
print()



#%%
print("VALORES IMPARES")
div_zero = [x for x in range(1,100)if x%3 ==0]
print(f"LISTA TOTAL: {div_zero}")
print(f"TOTAL: {len(div_zero)}")

print("VALORES PRIMOS")

primos_a = [x for x in range(1,100) if len([x for x in range(x) if y%x == 0])]

print(f"LISTA TOTAL: {primos_a}")
print(f"TOTAL: {len(primos_a)}")

#%%

for x in range(10):
    if x <8 ==1:
        print(x)

import time as t
        
n_itens = 15

def fat(y):
    fat = [y for y in range(y)]
    print(y)
    for x in fat:
        print(x *y)
        t.sleep(1)
        
get(10)