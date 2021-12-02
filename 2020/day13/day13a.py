from math import inf

n, bs = open("inputa.txt").readlines()

n = int(n)
bs = list(map(int, filter(lambda x: x != "x", bs.split(","))))

bb, bd = inf, inf

for b in bs:
    a, r = divmod(n, b)

    if b - r < bd:
        bb = b
        bd = b - r

print(bb * bd)