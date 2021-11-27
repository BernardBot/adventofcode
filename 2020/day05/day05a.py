lines = open("inputa.txt").read().splitlines()

def decode(line):
    return line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1")

print(max(int(decode(line), 2) for line in lines))

