import sys

xs = []
ys = []
for line in sys.stdin.readlines():
    x, y = line.split()
    xs.append(int(x))
    ys.append(int(y))

xs = sorted(xs)
ys = sorted(ys)

sum = 0
for x, y in zip(xs, ys):
    sum += abs(x - y)
print(sum)
