import sys

score = 0
for line in sys.stdin.readlines():
    l, r = line.strip().split(',')
    a, b = map(int, l.split('-'))
    x, y = map(int, r.split('-'))
    if (a <= x and x <= b) or (a <= y and y <= b):
        score += 1
    elif (x <= a and a <= y) or (y <= a and a <= y):
        score += 1
print(score)
