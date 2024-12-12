import sys

grid = sys.stdin.read().strip().split('\n')
width = len(grid[0])
height = len(grid)

moves = ((1, 0), (0, 1), (-1, 0), (0, -1))

def search(x, y):
    t = grid[y][x]
    area = list()
    perimeter = list()

    def _search(x, y):
        if (x, y) in area:
            return
        area.append((x, y))
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and grid[ny][nx] == t:
                _search(nx, ny)
            else:
                perimeter.append((nx, ny))

    _search(x, y)
    return area, perimeter

visited = set()
score = 0
for y in range(height):
    for x in range(width):
        if (x, y) in visited:
            continue
        area, perimeter = search(x, y)
        for coord in area:
            visited.add(coord)
        score += len(area) * len(perimeter)
print(score)
