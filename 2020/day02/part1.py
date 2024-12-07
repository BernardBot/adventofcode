lines = open("inputa.txt").readlines()

c = 0

for line in lines:
    rng, let, pwd = line.split()

    lo, hi = map(int, rng.split("-"))
    let = let[0]

    if lo <= pwd.count(let) <= hi:
        c += 1

print(c)