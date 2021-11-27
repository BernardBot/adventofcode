lines = open("inputb.txt").read().splitlines()

height = len(lines)
width = len(lines[0])

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

r = 1

for dx, dy in slopes:
    x = 0
    y = 0
    c = 0
    
    while y < height:
        if lines[y][x] == "#":
            c += 1
        x = (x + dx) % width
        y += dy

    r *= c

print(r)