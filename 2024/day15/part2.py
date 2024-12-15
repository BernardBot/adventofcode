import sys

grid, moves = sys.stdin.read().strip().split('\n\n')

symbolmap = {
    '#': '##',
    'O': '[]',
    '@': '@.',
    '.': '..',
}

grid = [list(''.join(symbolmap[s] for s in row)) for row in grid.split('\n')]
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
    if move in '<>':
        while grid[ny][nx] in '[]':
            nx += dx
        if grid[ny][nx] == '.':
            while (nx, ny) != (sx, sy):
                grid[ny][nx] = grid[ny][nx - dx]
                nx -= dx
            grid[sy][sx] = '.'
            sx, sy = sx + dx, sy + dy
        continue
    
    def search():
        layer = [(sx, sy)]
        moves = []
        while layer:
            next_layer = []
            for x, y in layer:
                tx, ty = x + dx, y + dy
                if grid[ty][tx] == '#':
                    return None

                moves.append(((x, y), (tx, ty), grid[y][x]))
                if grid[ty][tx] in '[]':
                    next_layer.append((tx, ty))
                    if grid[ty][tx] != grid[y][x]:
                        dtx = 1 if grid[ty][tx] == '[' else -1
                        next_layer.append((tx + dtx, ty))

            layer = next_layer
        return moves
    
    moves = search()
    if moves is None:
        continue
    for (fx, fy), (tx, ty), v in moves:
        grid[fy][fx] = '.'
    for (fx, fy), (tx, ty), v in moves:
        grid[ty][tx] = v
    sx, sy = nx, ny

score = 0
for x in range(width):
    for y in range(height):
        if grid[y][x] == '[':
            score += x + y * 100
print(score)
