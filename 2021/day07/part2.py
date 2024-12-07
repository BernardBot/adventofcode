ns = list(map(int, open('inputb.txt').read().split(',')))

m = max(ns)
b = 1e20
for i in range(m+1):
    b = min(b, sum(map(lambda n: sum(range(abs(n - i) + 1)), ns)))
print(b)