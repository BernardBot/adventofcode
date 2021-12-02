n, bs = open("inputb.txt").readlines()

bs = [int(x) if x != "x" else x for x in bs.split(",")]

ns = []
ds = []
c = 1
for b in bs[1:]:
    if b != "x":
        ns.append(b)
        ds.append(b - c)
    c += 1

def foo(a, b, m):
    # solve: a * x = b mod m
    for i in range(m):
        if (a * i) % m == b:
            return i

m = int(bs[0])
b = 0

for n, d in zip(ns, ds):
    r = foo(m, (d - b) % n, n)
    b += r * m
    m *= n
print(b)
    
# see: https://brilliant.org/wiki/chinese-remainder-theorem/
# see: https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html

# x = 0 mod 17
# x = 11 mod 13
# x = 16 mod 19