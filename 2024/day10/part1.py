import sys

grid = sys.stdin.read().strip().split('\n')
width = len(grid[0])
height = len(grid)

starts = []
for y in range(height):
    for x in range(width):
        if grid[y][x] == '0':
            starts.append((x, y))

moves = ((1, 0), (0, 1), (-1, 0), (0, -1))

def search(x, y):
    if (x, y) in visited:
        return 0
    visited.add((x, y))
    if grid[y][x] == '9':
        return 1
    score = 0
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < width and 0 <= ny < height:
            if ord(grid[ny][nx]) - ord(grid[y][x]) == 1:
                score += search(nx, ny)
    return score

score = 0
for sx, sy in starts:
    visited = set()
    score += search(sx, sy)
print(score)
