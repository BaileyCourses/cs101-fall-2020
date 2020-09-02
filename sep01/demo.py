#
# August is gone, September is upon us!
#
# September 1, 2020
#

from turtle import *
from time import sleep
from random import randrange

def start():
    fred = Turtle()
    fred.speed(2)
    shadow = fred.clone()
    shadow.pencolor("white")
    shadow.width(4)
    shadow.hideturtle()
    last = fred.position()
    head = fred.heading()
    lastdist = 0
    for _ in range(100):
        dist = randrange(25, 100)
        fred.setheading(randrange(360))
        fred.forward(dist)
        shadow.setheading(head)
        shadow.forward(lastdist)
        last = fred.position()
        head = fred.heading()
        lastdist = dist

if __name__ == "__main__":
    start()