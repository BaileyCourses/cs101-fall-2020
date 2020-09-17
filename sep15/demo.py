import random

def main():
    values = [29, 43, 78, 12, 3, 5, 3, 6, 7, 21]
    
    printList(values)
    print()
    printList([1, 2, 3])

def printList(vlist):
    for value in vlist:
        print(value)


def main_():
    count = 0
    for _ in range(60000):
        dieA = random.randrange(200)
        dieB = random.randrange(200)
        if dieA == dieB:
            count += 1
#            print("You rolled double", dieA, "s!")
    print("You rolled", count, "doubles")
        
def oldoldoldmain():
    fruits = ["apple", "banana", "pear", "durian", "kiwi"]
    
    for fruit in fruits:
        if len(fruit) < 5:
            print(fruit)
    

def oldoldmain():
    age = int(input("How old are you? "))
    
    if 2 < age or age > 90:
        print("You not middle aged!")
    else:
        print("Livin' the life!")

def oldmain():
    fruits = ["apple", "banana", "pear", "durian", "kiwi"]
    
    for fruit in fruits[::-1]:
        print(fruit)
    
if __name__ == "__main__":
    main()