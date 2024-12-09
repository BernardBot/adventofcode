import sys

grid = sys.stdin.read().strip().split('\n')
width = len(grid[0])
height = len(grid)

def get(x, y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return "("
    return grid[y][x]

def get_neighbours(x, y):
    return (
        get(x - 1, y - 1) + get(x, y - 1) + get(x + 1, y - 1) +
        get(x - 1, y)                     + get(x + 1, y)     +
        get(x - 1, y + 1) + get(x, y + 1) + get(x + 1, y + 1)
    )

score = 0
for y in range(height):
    x = 0
    while x < width:
        val = ""
        while get(x, y) in ".+/&-@#=*$%":
            x += 1
        while get(x, y) in "0123456789":
            val += get(x, y)
            x += 1
        valid = False
        for tx in range(x - len(val), x):
            if any(char in "+/&-@#=*$%" for char in get_neighbours(tx, y)):
                valid = True
        if valid:
            score += int(val)

print(score)
