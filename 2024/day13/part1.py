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

    for i in range(100):
        for j in range(100):
            x = ax * i + bx * j
            y = ay * i + by * j
            if x == px and y == py:
                score += 3 * i + j
print(score)
