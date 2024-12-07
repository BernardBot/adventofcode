import sys

score = 0
for line in sys.stdin.readlines():
    l, r = line.strip().split(',')
    a, b = map(int, l.split('-'))
    x, y = map(int, r.split('-'))
    if a <= x and y <= b:
        score += 1
    elif x <= a and b <= y:
        score += 1
print(score)