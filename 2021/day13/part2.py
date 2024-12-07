lines = open("inputb.txt").readlines()

ns = set()
folds = []

for line in lines:
    if line.startswith("fold"):
        fold, along, equals = line.split()
        xy, val = equals.split("=")
        folds.append((xy, int(val)))

    if "," in line:
        x, y = map(int, line.split(","))
        ns.add((x, y))

for fold in folds:
    xy, val = fold
    new_ns = set()
    if xy == "x":
        for x, y in ns:
            if x > val:
                new_ns.add((2 * val - x, y))
            elif x < val:
                new_ns.add((x, y))
    if xy == "y":
        for x, y in ns:
            if y < val:
                new_ns.add((x, y))
            if y > val:
                new_ns.add((x, 2 * val - y))
    ns = new_ns

xmax = max(map(lambda n: n[0], ns))
ymax = max(map(lambda n: n[1], ns))

for y in range(ymax + 1):
    for x in range(xmax + 1):
        if (x, y) in ns:
            print("#", end="")
        else:
            print(".", end="")
    print()
