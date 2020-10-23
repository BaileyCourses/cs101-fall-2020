import csv

def readCSV(filename):
    with open(filename, 'r', encoding = 'utf-8-sig') as fileHandle:
        reader = csv.reader(fileHandle)
        grid = []
        for row in reader:
            grid.append(row)
        return grid

def encloseRoom(room):
    room = [['O'] * len(room[0])] + room + [['O'] * len(room[0])]
    for r in range(len(room)):
        room[r] = ['O'] + room[r] + ['O']
        
    return room

def findVacuum(room):
    for r in range(len(room)):
        for c in range(len(room[r])):
            if room[r][c] == "V":
                return (r, c)
    print("Didn't find the vacuum!")

def printGrid(grid):
    for row in grid:
        print(row)
        
def moveVacuum(room, vacLoc, dir):
    (r, c) = vacLoc
    
    if dir == "U":
        newLoc = (r - 1, c)
        
    elif dir == "D":
        newLoc = (r + 1, c)
        
    elif dir == "L":
        newLoc = (r, c - 1)

    elif dir == "R":
        newLoc = (r, c + 1)
        
    (r, c) = newLoc
        
    if room[r][c] == "O":
        newLoc = vacLoc

    (r, c) = vacLoc
    room[r][c] = "C"

    (r, c) = newLoc
    room[r][c] = "V"
    
    return newLoc

def findClosestDirt(room, vacLoc):
    vr, vc = vacLoc
    minDist = len(room) + len(room[0])
    minLoc = vacLoc
    for r in range(len(room)):
        for c in range(len(room[r])):
            if room[r][c] == "D":
                dist = abs(r - vr) + abs(c - vc)
                if dist < minDist:
                    minDist = dist
                    minLoc = (r, c)
                    
    return minLoc
        
def first():
    grid = readCSV("room.csv")
    grid = encloseRoom(grid)
    printGrid(grid)
    (r, c) = findVacuum(grid)
    (dr, dc) = findClosestDirt(grid, (r, c))
    (r, c) = moveVacuum(grid, (r, c), "L")
    (r, c) = moveVacuum(grid, (r, c), "L")
    (r, c) = moveVacuum(grid, (r, c), "L")
    print()
    printGrid(grid)
#    print(dr, dc)

if __name__ == "__main__":
    first()
