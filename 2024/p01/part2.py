import sys

xs = []
ys = []
for line in sys.stdin.readlines():
    x, y = line.split()
    xs.append(int(x))
    ys.append(int(y))

sum = 0
for x in xs:
    c = ys.count(x)
    sum += c * x

print(sum)
