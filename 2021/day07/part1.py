ns = list(map(int, open('inputa.txt').read().split(',')))

m = max(ns)

b = 1e20

for i in range(-m, m+1):
    b = min(b, sum(map(lambda n: abs(n - i), ns)))
print(b)