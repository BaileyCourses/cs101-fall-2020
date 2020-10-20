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
    (r, c) = findVacuum(grid)
    (dr, dc) = findClosestDirt(grid, (r, c))
    print(dr, dc)

if __name__ == "__main__":
    first()
