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

def search(x, y, dist):
    if grid[y][x] == '#':
        return
    if (x, y) in mem and mem[(x, y)] <= dist:
        return
    mem[(x, y)] = dist
    for dx, dy in moves:
        search(x + dx, y + dy, dist + 1)

search(sx, sy, 0)

score = 0
cheatdist = 20
for y in range(height):
    for x in range(width):
        if grid[y][x] != '#':
            for dx in range(-cheatdist, cheatdist + 1):
                for dy in range(-cheatdist, cheatdist + 1):
                    dist = abs(dx) + abs(dy)
                    if dist <= cheatdist:
                        nx, ny = x + dx, y + dy
                        if (nx, ny) in mem:
                            if mem[(nx, ny)] - mem[(x, y)] >= 100 + dist:
                                score += 1
print(score)
