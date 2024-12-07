import sys

input = sys.stdin.read()

rows = input.strip().split("\n")
width = len(rows[0])
height = len(rows)

def get(x, y):
    if x < 0 or x >= width or y < 0 or y >= height:
        return "."
    return rows[y][x]

score = 0
for x in range(width):
    for y in range(height):
        d1 = get(x - 1, y - 1) + get(x, y) + get(x + 1, y + 1)
        d2 = get(x - 1, y + 1) + get(x, y) + get(x + 1, y - 1)

        if (d1 == "MAS" or d1 == "SAM") and (d2 == "MAS" or d2 == "SAM"):
            score += 1

print(score)
