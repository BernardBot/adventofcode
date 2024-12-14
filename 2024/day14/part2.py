import sys

width = 101
height = 103

plcs = []
vels = []
for line in sys.stdin.read().strip().split('\n'):
    ps, vs = line.split(' ')
    px, py = [int(p) for p in ps[2:].split(',')]
    vx, vy = [int(v) for v in vs[2:].split(',')]

    plcs.append((px, py))
    vels.append((vx, vy))

grid = []
for y in range(height):
    grid.append([])
    for x in range(width):
        grid[-1].append('.')

t = 0
while True:
    for px, py in plcs:
        grid[py][px] = '#'
    if '#########' in '\n'.join(''.join(row) for row in grid):
        print(t)
        break
    for px, py in plcs:
        grid[py][px] = '.'

    new_plcs = []
    for (px, py), (vx, vy) in zip(plcs, vels):
        new_plcs.append(((px + vx) % width, (py + vy) % height))
    plcs = new_plcs
    t += 1
