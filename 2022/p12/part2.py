import sys
sys.setrecursionlimit(10000)

grid = sys.stdin.read().strip().split("\n")
width = len(grid[0])
height = len(grid)

starting_positions = []
for x in range(width):
    for y in range(height):
        if grid[y][x] == "a":
            starting_positions.append((x, y))
        if grid[y][x] == "E":
            ex, ey = x, y

grid[ey] = grid[ey].replace('E', chr(ord('z') + 1))

mem = {}
for x in range(width):
    for y in range(height):
        mem[(x, y)] = float("inf")

def search(x, y, dist):
    mem[(x, y)] = dist
    if (x, y) == (ex, ey):
        return dist
    best = float("inf")
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if (
            (nx, ny) in mem and
            ord(grid[ny][nx]) - ord(grid[y][x]) < 2 and
            mem[(nx, ny)] > dist + 1
        ):
            best = min(best, search(nx, ny, dist+1))
    return best

results = []
for sx, sy in starting_positions:
    result = search(sx, sy, 0)
    results.append(result)
print(min(results))
