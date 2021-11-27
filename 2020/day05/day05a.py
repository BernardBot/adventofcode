lines = open("inputa.txt").read().splitlines()

def decode(line):
    return int(line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2)

print(max(map(decode, lines)))

