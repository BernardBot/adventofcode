import sys

score = 0
type_count_max = {'red': 12, 'green': 13, 'blue': 14}
for line in sys.stdin.readlines():
    turns = line.split()[2:]
    type_count = {'red': 0, 'green': 0, 'blue': 0}
    for i in range(len(turns) // 2):
        val = int(turns[2 * i])
        type = turns[2 * i + 1].rstrip(',;')
        type_count[type] = max(type_count[type], val)
    power = 1
    for val in type_count.values():
        power *= val
    score += power
print(score)
