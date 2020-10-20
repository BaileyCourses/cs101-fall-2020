import random

def make2D(rows, cols, bounds = (1, 11)):
    lower, upper = bounds

    result = []
    
    for r in range(rows):
        result.append([])
        for c in range(cols):
            result[-1].append(random.randrange(lower, upper))
    
    return result[1:]

def printGrid(grid):
    for row in grid:
        print(row)
        
def find(grid, target):
    for r in range(len(grid)):
        for c in range(len(grid[0])):            
            if grid[r][c] == target:
                return (r, c)
    return (-1, -1)

def start():
    grid = make2D(10, 8, (4, 8))  
    printGrid(grid)
    print(find(grid, 10))
    
    
if __name__ == "__main__":
    start()
