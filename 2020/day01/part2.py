ns = set(map(int, open("inputa.txt").readlines()))

for n in ns:
    for m in ns:
        if 2020 - n - m in ns:
            print(m * n * (2020 - n - m))
            exit()