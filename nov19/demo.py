import time
import random

def makeList(count, low = 0, high = 1000):
    values = []
    for _ in range(count):
        value = random.randrange(low, high)
        values.append(value)

    return values


def occursBad(c, s):
    return c in s

def occurs(c, s):
    for letter in s:
        if letter == c:
            return True
    return False

def inBoth(listA, listB):
    result = []

    for value in listA:
        if value in listB:
            result.append(value)
    return result

def twoInARow(grid):
    for row in grid:
        for i in range(1, len(row)):
            if row[i - 1] == row[i]:
                return True
    return False

def search(value, lst):
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return None

def first():
    grid = [ [1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]
    ]
#    print(twoInARow(grid))

    lst = makeList(10)
    lst.insert(random.randrange(len(lst)), 5)
    lst = sorted(lst)
    print(lst)
    print(search(5, lst))
          
          
#    print(inBoth([1, 2, 3], [3, 4, 1]))
    
if __name__ == "__main__":
    first()
