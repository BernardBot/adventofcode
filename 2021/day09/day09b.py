lines = open("inputb.txt").readlines()

w = len(lines[0].strip())
h = len(lines)

def neig(x, y):
    if x < 0 or x >= w or y < 0 or y >= h:
        return {}

    xp = x + 1 if x < w - 1 else x - 1
    xm = x - 1 if x > 0     else x + 1
    yp = y + 1 if y < h - 1 else y - 1
    ym = y - 1 if y > 0     else y + 1

    cxp = int(lines[y][xp])
    cxm = int(lines[y][xm])
    cyp = int(lines[yp][x])
    cym = int(lines[ym][x])

    # change to dict
    return set([
        (xp, y),
        (xm, y),
        (x, yp),
        (x, ym),
    ])

visited = set()
basins = []
for x in range(w):
    for y in range(h):
        c = int(lines[y][x])
        if c == 9 or (x, y) in visited:
            continue
        gs = neig(x, y)
        basin = set([(x, y)])
        while gs:
            x, y = gs.pop()
            c = int(lines[y][x])
            if c == 9:
                continue
            basin.add((x, y))
            gs = (gs | neig(x, y)) - basin
            visited |= basin
        basins.append(basin)

# too low!
ls = sorted(map(len, basins))
c = 1
for l in ls[-3:]:
    c *= l
print(c)