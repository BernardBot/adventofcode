ns = list(map(int, open("inputa.txt").readlines()))

print(sum(ns[i+1]>ns[i] for i in range(len(ns) - 1)))