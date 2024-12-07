from collections import defaultdict

lines = open("inputa.txt").readlines()

ls = []
for line in lines:
    f, t = line.split("->")
    x1, y1 = f.strip().split(",")
    x2, y2 = t.strip().split(",")
    ls.append((int(x1), int(y1), int(x2), int(y2)))

d = defaultdict(int)
for x1, y1, x2, y2 in ls:
    if x1 == x2:
        a = min(y1, y2)
        b = max(y1, y2)
        for i in range(a, b+1):
            d[(x1, i)] += 1
    elif y1 == y2:
        a = min(x1, x2)
        b = max(x1, x2)
        for i in range(a, b+1):
            d[(i, y1)] += 1

c = 0
for k in d:
    if d[k] > 1:
        c += 1
print(c)