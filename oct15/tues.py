import csv

def zip(listA, listB):

    # Ensure that list A is no longer than list B

    listA = listA[:len(listB)]
    
    result = []

    # For each element of listA, form a list of that element and the
    # corresponding element in listB. This requires that listB have length
    # at least as long as listA.

    for i in range(len(listA)):
        result.append([listA[i], listB[i]])
    
    return result

def unzip(lst, fill = None):
    listA = []
    listB = []
    
    for item in lst:
        a, b = (item + [fill, fill])[:2]
        listA.append(a)
        listB.append(b)
        
    return listA, listB
        
def start():
    fd = open("cs101grades.csv", "r")
    reader = csv.reader(fd)
    
    # Q: I am a bit confused about Header. Why we put a None in the function.

    header = next(reader, None)
    
    sheet = []
    for row in reader:
        sheet.append(row)

    grid = []
    for r in range(len(sheet)):
        grid.append([])
        for c in range(len(sheet[0])):
            grid[-1].append(sheet[r][c])

    #left = [1, 2, 3, 4]
    #right = [5, 6, 7, 8]

    #print(zip(left, right))

    result = zip(sheet[3], sheet[4][:-3])
    listA, listB = unzip(result)
    
    #print(listA)
    #print(listB)
    
    zipped = [
        [1, 3],
        [2],
        [],
        [5, 6, 7]
        ]
    print(unzip(zipped, 0))
    print(unzip([], 0))


if __name__ == "__main__":
    start()
