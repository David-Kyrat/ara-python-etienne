from random import randint

de = randint(1,6)   
nb = 0

while de != nb :
    nb = int(input("prendre un nombre"))      
    if nb != de: 
        print("pas le bon nombre")
    else :
        print("bravo")
