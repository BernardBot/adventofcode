import sys
sys.setrecursionlimit(10000)

falling_bytes = []
for line in sys.stdin.readlines():
    x, y = [int(v) for v in line.split(',')]
    falling_bytes.append((x, y))

width = 71
height = 71

lo = 0
hi = len(falling_bytes)
while True:
    i = (lo + hi) // 2
    grid = []
    for y in range(height):
        grid.append([])
        for x in range(width):
            grid[y].append('.')

    for x, y in falling_bytes[:i]:
        grid[y][x] = '#'

    mem = {}
    def search(x, y, dist):
        if x < 0 or x >= width or y < 0 or y >= height:
            return
        if grid[y][x] == '#':
            return
        if (x, y) in mem and mem[(x, y)] <= dist:
            return
        mem[(x, y)] = dist
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            search(x + dx, y + dy, dist + 1)

    search(0, 0, 0)
    if lo >= hi:
        x, y = falling_bytes[i - 1]
        print(f'{x},{y}')
        break

    if (width - 1, height - 1) in mem:
        lo = i + 1
    else:
        hi = i
