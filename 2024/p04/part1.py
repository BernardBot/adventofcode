import sys

input = sys.stdin.read()

rows = input.strip().split("\n")
width = len(rows[0])
height = len(rows)

def get(x, y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return "."
    return rows[y][x]

offset = (
    (1, 0),
    (0, 1),
    (1, 1),
    (1, -1),
)

score = 0
for x in range(width):
    for y in range(height):
        for dx, dy in offset:
            s = ""
            for i in range(4):
                s += get(x + dx * i, y + dy * i)
            if s == "XMAS" or s[::-1] == "XMAS":
                score += 1

print(score)
