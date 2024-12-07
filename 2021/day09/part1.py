lines = open("inputa.txt").readlines()

w = len(lines[0].strip())
h  = len(lines)

ns = []
for x in range(w):
    for y in range(h):
        c = int(lines[y][x])

        xp = x + 1 if x < w - 1 else x - 1
        xm = x - 1 if x > 0     else x + 1
        yp = y + 1 if y < h - 1 else y - 1
        ym = y - 1 if y > 0     else y + 1

        cxp = int(lines[y][xp])
        cxm = int(lines[y][xm])
        cyp = int(lines[yp][x])
        cym = int(lines[ym][x])

        if c < cxp and c < cxm and c < cyp and c < cym:
            ns.append(c)

print(sum(ns) + len(ns))