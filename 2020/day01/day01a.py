ns = set(map(int, open("inputa.txt").readlines()))

for n in ns:
    if 2020 - n in ns:
        print(n * (2020 - n))
        exit()