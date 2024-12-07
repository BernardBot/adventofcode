lines = open("inputb.txt").readlines()

m = len(lines[0].strip())

for j in range(m):
    c = 0
    for line in lines:
        if line[j] == "1":
            c += 1

    if c * 2 >= len(lines):
        a = "1"
    else:
        a = "0"

    lines = list(filter(lambda line: line[j] == a, lines))
    
    if len(lines) == 1:
        ans = int(lines[0], 2)
        break


lines = open("inputb.txt").readlines()

n = len(lines)
m = len(lines[0].strip())

for j in range(m):
    c = 0
    for line in lines:
        if line[j] == "1":
            c += 1

    if c * 2 < len(lines):
        a = "1"
    else:
        a = "0"

    lines = list(filter(lambda line: line[j] == a, lines))
    
    if len(lines) == 1:
        print(ans * int(lines[0], 2))
        break