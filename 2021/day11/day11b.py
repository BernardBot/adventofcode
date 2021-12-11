lines = open("inputb.txt").readlines()

grid = []
for line in lines:
    l = []
    for c in line:
        try:
            l.append(int(c))
        except:
            pass
    grid.append(l)

w = len(grid[0])
h = len(grid)

n = 100

def bounds(x, y):
    return x >= 0 and x < w and y >= 0 and y < h

def neig(x, y):
    return list(filter(lambda x: bounds(*x), [
        (x+1, y),
        (x-1, y),
        (x, y+1),
        (x, y-1),
        (x+1, y+1),
        (x-1, y-1),
        (x-1, y+1),
        (x+1, y-1),
    ]))

i = 1
while True:
    for x in range(w):
        for y in range(h):
            grid[y][x] += 1
    
    flash_count = 0
    flashed = False

    while True:
        for x in range(w):
            for y in range(h):
                if grid[y][x] > 9:
                    for nx, ny in neig(x, y):
                        if grid[ny][nx] != 0:
                            grid[ny][nx] += 1
                    grid[y][x] = 0
                    flashed = True
                    flash_count += 1

        if flashed == False:
            break
        flashed = False

    if flash_count == w * h:
        print(i)
        break
    i += 1
