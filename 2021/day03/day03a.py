lines = open("inputa.txt").readlines()

n = len(lines)
m = len(lines[0].strip())

bs = [0] * m

for line in lines:
    for i, b in enumerate(line.strip()):
        bs[i] += int(b)

x = "".join(str(round(b / n)) for b in bs)
y = "".join(str(1 - round(b / n)) for b in bs)

print(int(x, 2) * int(y, 2))