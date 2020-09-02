#
# more Python!
#
# August 27, 2020
#

from turtle import *

def main():
    #input()                             # Wait for the user to press enter
    gill = Turtle()

    sideLength = 50
    sides = 200
    
    for _ in range(sides):
        gill.forward(sideLength)
        gill.left(360 / sides)

    gill.up()
    gill.goto(-200, -200)
    gill.down()
    
    for _ in range(3):
        gill.forward(sideLength)
        gill.left(120)


if __name__ == "__main__":
    main()
