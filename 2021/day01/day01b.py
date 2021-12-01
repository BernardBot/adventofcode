ns = list(map(int, open("inputb.txt").readlines()))

print(sum(sum(ns[i+1:i+4])>sum(ns[i:i+3]) for i in range(len(ns))))