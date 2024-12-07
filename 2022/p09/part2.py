import sys

def sign(x):
    if x == 0:
        return 0
    if x > 0:
        return 1
    return -1

def move_tail(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    if abs(dx) > 1 or abs(dy) > 1:
        b[0] += sign(dx)
        b[1] += sign(dy)

visited = set()
rope = [[0, 0] for _ in range(10)]
for line in sys.stdin.readlines():
    dir, size = line.split()
    size = int(size)
    for _ in range(size):
        if dir == "R": rope[0][0] += 1
        if dir == "L": rope[0][0] += -1
        if dir == "U": rope[0][1] += 1
        if dir == "D": rope[0][1] += -1
        for i in range(1, len(rope)):
            move_tail(rope[i - 1], rope[i])
        visited.add(tuple(rope[-1]))
print(len(visited))
