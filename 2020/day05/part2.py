lines = open("inputb.txt").read().splitlines()

def decode(line):
    return int(line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2)

ids = set(map(decode, lines))
rng = set(range(min(ids), max(ids) + 1))

print(list(rng - ids)[0])
