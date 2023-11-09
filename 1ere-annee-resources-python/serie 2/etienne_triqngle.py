from turtle import *

n = int(input("prendre un nombre?"))
for k in range(n):
    for i in range(3):
        forward(65)
        left(120)
    up()
    forward(200)
    down()
    