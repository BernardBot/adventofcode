lines = open("inputa.txt").readlines()

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

xy, val = folds[0]
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
print(len(set(ns)))
