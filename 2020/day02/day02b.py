lines = open("inputb.txt").readlines()

c = 0

for line in lines:
    rng, let, pwd = line.split()

    lo, hi = map(int, rng.split("-"))
    let = let[0]

    if (pwd[lo - 1] == let) ^ (pwd[hi - 1] == let):
        c += 1

print(c)