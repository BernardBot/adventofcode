ns = list(map(int, open('inputa.txt').read().split(',')))
c = 80

for _ in range(c):
    new_ns = []
    for n in ns:
        if n == 0:
            new_ns.append(6)
            new_ns.append(8)
        else:
            new_ns.append(n - 1)
    ns = new_ns

print(len(ns))