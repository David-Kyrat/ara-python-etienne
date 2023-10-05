from turtle import*

def carre(taille,couleur):
    down()
    color(couleur)
    for i in range (4):
        forward (taille)
        left (90)
    up()    

def triangle(taille):
    down()
    for j in range(3):
        forward(taille)
        left(120)
    up()
##########################################
    
for i in range(25,60,5):
    carre(i,red)
    forward(i+5)
    down()
    triangle(i)
    forward(i+5)
done()
