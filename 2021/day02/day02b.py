lines = open("inputb.txt").readlines()

x = 0
y = 0
a = 0

for line in lines:
    op, i = line.split()
    i = int(i)

    if "forward" in op:
        x += i
        y += a * i
    elif "down" in op:
        a += i
    elif "up" in op:
        a -= i


print(x * y)