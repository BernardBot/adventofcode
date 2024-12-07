import sys

grid = sys.stdin.read().strip().split("\n")
width = len(grid[0])
height = len(grid)

obstacles = []
for x in range(width):
    for y in range(height):
        if grid[y][x] == "^":
            sx, sy = x, y

x, y = sx, sy
dx, dy = 0, -1
visited = set()
while True:
    while grid[y][x] != "#":
        visited.add((x, y))
        x += dx
        y += dy
        if x < 0 or x >= width or y < 0 or y >= height:
            print(len(visited))
            exit()
    x -= dx
    y -= dy
    dx, dy = -dy, dx
