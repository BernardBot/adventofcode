import sys

grid, moves = sys.stdin.read().strip().split('\n\n')

grid = [list(row) for row in grid.split('\n')]
width = len(grid[0])
height = len(grid)

moves = moves.replace('\n', '')

for x in range(width):
    for y in range(height):
        if grid[y][x] == '@':
            sx, sy = x, y

directions = {
    '^': (0, -1),
    'v': (0, 1),
    '>': (1, 0),
    '<': (-1, 0),
}

for move in moves:
    dx, dy = directions[move]
    nx, ny = sx + dx, sy + dy
    while grid[ny][nx] == 'O':
        nx += dx
        ny += dy
    if grid[ny][nx] == '.':
        grid[ny][nx] = 'O'
        grid[sy][sx] = '.'
        sx, sy = sx + dx, sy + dy
        grid[sy][sx] = '@'

score = 0
for x in range(width):
    for y in range(height):
        if grid[y][x] == 'O':
            score += x + y * 100

print(score)