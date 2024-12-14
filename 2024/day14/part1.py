import sys

width = 101
height = 103

coords = []
for line in sys.stdin.read().strip().split('\n'):
    ps, vs = line.split(' ')
    px, py = [int(p) for p in ps[2:].split(',')]
    vx, vy = [int(v) for v in vs[2:].split(',')]

    for _ in range(100):
        px += vx
        py += vy
        px %= width
        py %= height

    coords.append((px, py))

q_count = [0, 0, 0, 0]
for x, y in coords:
    if x < width // 2 and y < height // 2:
        q_count[0] += 1
    elif x < width // 2 and y > height // 2:
        q_count[1] += 1
    elif x > width // 2 and y < height // 2:
        q_count[2] += 1
    elif x > width // 2 and y > height // 2:
        q_count[3] += 1

score = 1
for count in q_count:
    score *= count
print(score)
