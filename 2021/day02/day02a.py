lines = open("inputa.txt").readlines()

x = 0
y = 0

for line in lines:
    op, i = line.split()
    i = int(i)

    if "forward" in op:
        x += i
    elif "down" in op:
        y += i
    elif "up" in op:
        y -= i

print(x * y)