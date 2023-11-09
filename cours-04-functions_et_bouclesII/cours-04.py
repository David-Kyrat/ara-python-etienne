from copy import deepcopy
from re import T
from sys import builtin_module_names

orig = {"lu": "lundi", "me": "mercredi", "ma": "mardi", "me": "mercredi", "je": "jeudi"}

keys = list(orig.keys())
values = list(orig.values())

a = {"lu": "lundi"}
dicts: list[dict] = [deepcopy(a)]

for key, val in zip(keys, values):
    a[key] = val
    dicts.append(deepcopy(a))


def add(a, b):
    print(a, b)
    return


print("test")

# ===========================================

# EXO: print la taille de chaque dictionnaire en utilisant une boucle for

# ? On itère sur dicts
# ? la variable c'est le truc avant le "in" (ici elem)
for elem in dicts:
    print(elem, len(elem))
print("=========================\n\n")

# Definir une fonction qui retourne le resultat de la multiplication de 2 nombres
# Puis appeler la fonction et print le resultat


def mul(a, b):
    res = a * b
    return res


def mul2(a, b):
    return a * b


a = 5
b = 8

c = mul(a, b)
print(c)
print("=========================\n\n")

def example_return_loop(my_list):
    for i in range(len(my_list)):
        print(my_list[i])
        if i >= 2:
            return
        
        if i > 2: 
            print("This is never executed either")
    print("This is never executed")


test = [1, 2, 3, 4, 5]

example_return_loop(test)