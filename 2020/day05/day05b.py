lines = open("inputb.txt").read().splitlines()

def decode(line):
    return line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")

ids = set(int(decode(line), 2) for line in lines)
rng = set(range(min(ids), max(ids) + 1))

print(list(rng - ids)[0])
