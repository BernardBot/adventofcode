import sys

rounds = sys.stdin.read().strip().split('\n\n')

score = 0
for round in rounds:
    lines = round.split('\n')
    ax, ay = lines[0].split(':')[1].split(',')
    ax = int(ax.split('+')[1])
    ay = int(ay.split('+')[1])

    bx, by = lines[1].split(':')[1].split(',')
    bx = int(bx.split('+')[1])
    by = int(by.split('+')[1])

    px, py = lines[2].split(':')[1].split(',')
    px = int(px.split('=')[1])
    py = int(py.split('=')[1])

    px += 10000000000000
    py += 10000000000000

    j = (py * ax - ay * px) / (-ay * bx + by * ax)
    i = (px - bx * j) / ax

    if i.is_integer() and j.is_integer():
        score += int(3 * i + j)
print(score)
