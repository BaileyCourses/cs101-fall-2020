import time
import random

def makeList(count, low = 0, high = 1000):
    values = []
    for _ in range(count):
        value = random.randrange(low, high)
        values.append(value)

    return values

def sorted(lst):
    for i in range(1, len(lst)):
        if lst[i - 1] > lst[i]:
            return False
    return True

def minIndex(lst):
    min = lst[0]
    index = 0
    
    for i in range(1, len(lst)):
        if lst[i] < min:
            min = lst[i]
            index = i
            
    return index

def selectionSort(values):
    for i in range(len(values) - 1):    # i is the index of the location to place the new sorted item
        index = minIndex(values[i:])
        
        tmp = values[i]
        values[i] = values[index + i]
        values[index + i] = tmp
        
    return values

def first():
    lst = makeList(100000)
#    print(lst)
    slst = selectionSort(lst)
#    print(slst)
    print(sorted(slst))

    
    
if __name__ == "__main__":
    first()
