import csv

def average(lists, col):
    sum = 0
    for row in range(len(lists)):
        sum += int(lists[row][col])
        
    ave = sum / len(lists)
    
    return ave
    
def zip(listA, listB):

    listA = listA[:len(listB)]
    
    result = []

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
    
    header = next(reader, None)
    
#    print(header)

    sheet = []
    for row in reader:
        sheet.append(row)

#    for r in range(len(sheet)):
#        print(sheet[r][0])
#    print (average(sheet, 4))

#    print(sheet)
    result = zip(sheet[3], sheet[4][:-3])
    listA, listB = unzip(result)
    
    print(listA)
    print(listB)
    
if __name__ == "__main__":
    start()
