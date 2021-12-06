ns = list(map(int, open('inputb.txt').read().split(',')))
d = { i : ns.count(i) for i in range(7)}

c = 256

for _ in range(c):
    new_d = { i : 0 for i in range(9) }
    for k, v in d.items():
        if k == 0:
            new_d[6] += v
            new_d[8] += v
        else:
            new_d[k - 1] += v
    d = new_d
print(sum(d.values()))