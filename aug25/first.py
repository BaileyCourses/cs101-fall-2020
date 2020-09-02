#
# A first program in Python!
#
# August 25, 2020
#

from turtle import *

def start():
    fred = Turtle()
#    fred.forward(100)
#    fred.left(90)
#    fred.forward(100)
#    fred.left(90)
#    fred.forward(100)
#    fred.left(90)
#    fred.forward(100)

    for _ in range(30):
        fred.forward(100)
        fred.left(120)
        fred.forward(100)
        fred.left(120)
        fred.forward(100)
        fred.left(175)



if __name__ == "__main__":
    start()