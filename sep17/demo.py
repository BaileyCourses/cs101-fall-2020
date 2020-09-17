def candidateParty(candidate):

    if candidate == "Biden":
        return "Democrat"
    elif candidate == "Trump":
        return "Republican"
    else:
        return "Independent"

# Counts the number of occurrences of things in a list

def occurrences(value, items):
    count = 0
    for item in items:
        if item == value:
            count += 1

    return count

def remove(value, items):
    newItems = []
    for item in items:
        if item == value:
            pass
        else:
            newItems.append(item)
    return newItems

import random

def start():
    numbers = []
    for _ in range(100000):
        numbers.append(random.randrange(500))
#    print(numbers)    
#    party = candidateParty("Trump")
#    print(party)
    count = occurrences(344, numbers)
    print(count)
    newNumbers = remove(344, numbers)
    count = occurrences(345, newNumbers)
    print(count)
    
if __name__ == "__main__":
    start()
    
