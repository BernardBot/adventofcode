import sys
import collections

grid = sys.stdin.read().strip().split('\n')
width = len(grid[0])
height = len(grid)

antennas_per_type = collections.defaultdict(list)

for x in range(width):
    for y in range(height):
        val = grid[y][x]
        if "a" <= val <= "z" or "A" <= val <= "Z" or "0" <= val <= "9":
            antennas_per_type[val].append((x, y))

locations = set()
for antennas in antennas_per_type.values():
    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            x1, y1 = antennas[i]
            x2, y2 = antennas[j]
            dx = x2 - x1
            dy = y2 - y1

            x = x1 - dx
            y = y1 - dy
            if 0 <= x < width and 0 <= y < height:
                locations.add((x, y))

            x = x2 + dx
            y = y2 + dy
            if 0 <= x < width and 0 <= y < height:
                locations.add((x, y))
            
print(len(locations))
