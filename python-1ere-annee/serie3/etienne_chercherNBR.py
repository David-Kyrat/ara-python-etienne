from random import randint

de = randint(1,100)
x = 0
print(de)
compteur = 0

while x != de:
    compteur=compteur+1    
    x = int(input("entez un nombre "))
    if de < x: 
        print("c'est moins")
    elif de > x: 
        print("c'est plus")
    else:
        print('tu as trouvé en tant d essais', compteur, )
    if compteur == 5:
        print("vous reste 5 essais")
    elif compteur == 10:
        print('trop d essais la reponse etait',(de))
        break
    if x == -1:
        print('tricheur la réponse est',(de))
        break