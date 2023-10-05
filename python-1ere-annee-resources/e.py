# sourcery skip: aug-assign, use-fstring-for-concatenation
nball = 20

j1 = input("joueur1 quel est ton nom?")
j2 = input("joueur2 quel est ton nom?")

nbtour = 0

while nball > 0:
    nbtour = nbtour + 1
    print("vous avez fait ", nbtour)

    a = int(input(j1 + " combien enleve tu d allumettes?"))
    nball = nball - a
    print("Il reste ", nball, " allumettes")
    if nball <= 0:
        print(j1, "a gagné!")
        break

    b = int(input(j2 + "combien enleve tu d allumettes?"))
    nball = nball - b
    print("Il reste ", nball, " allumettes")
    if nball <= 0:
        print(j2, " a gagné!")
        break
