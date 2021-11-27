lines = open("inputa.txt").read().splitlines()

height = len(lines)
width = len(lines[0])

x = 0
y = 0

dx = 3
dy = 1

c = 0

while y < height:
    if lines[y][x] == "#":
        c += 1
    x = (x + dx) % width
    y += dy

print(c)