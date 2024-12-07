import sys

grid = sys.stdin.read().strip().split("\n")
width = len(grid[0])
height = len(grid)

obstacles = []
for x in range(width):
    for y in range(height):
        if grid[y][x] == "^":
            sx, sy = x, y
        if grid[y][x] == ".":
            obstacles.append((x, y))

def is_loop():
    x, y = sx, sy
    dx, dy = 0, -1
    visited = set()
    while True:
        while grid[y][x] != "#":
            if (x, y, dx, dy) in visited:
                return True
            visited.add((x, y, dx, dy))
            x += dx
            y += dy
            if x < 0 or x >= width or y < 0 or y >= height:
                return False
        x -= dx
        y -= dy
        dx, dy = -dy, dx

score = 0
for x, y in obstacles:
    grid[y] = grid[y][:x] + "#" + grid[y][x+1:]
    score += is_loop()
    grid[y] = grid[y][:x] + "." + grid[y][x+1:]
print(score)
