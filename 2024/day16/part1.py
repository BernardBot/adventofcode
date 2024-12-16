import sys
sys.setrecursionlimit(10000)

grid = sys.stdin.read().strip().split('\n')
width = len(grid[0])
height = len(grid)

for x in range(width):
    for y in range(height):
        if grid[y][x] == 'S':
            sx, sy = x, y
        if grid[y][x] == 'E':
            ex, ey = x, y

moves = ((1, 0), (-1, 0), (0, 1), (0, -1))
mem = {}

def search(x, y, dx, dy, dist):
    if grid[y][x] == '#':
        return
    if (x, y) in mem and mem[(x, y)] <= dist:
        return
    mem[(x, y)] = dist
    for ndx, ndy in moves:
        nx = x + ndx
        ny = y + ndy
        ndist = dist + 1
        if (dx, dy) != (ndx, ndy):
            ndist += 1000
        search(nx, ny, ndx, ndy, ndist)

search(sx, sy, 1, 0, 0)
print(mem[(ex, ey)])
