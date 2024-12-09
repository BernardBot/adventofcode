import sys

score = 0
type_count_max = {'red': 12, 'green': 13, 'blue': 14}
for id, line in enumerate(sys.stdin.readlines()):
    turns = line.split()[2:]
    possible = True
    for i in range(len(turns) // 2):
        val = int(turns[2 * i])
        type = turns[2 * i + 1].rstrip(',;')
        if type_count_max[type] < val:
            possible = False
            break
    if possible:
        score += id + 1
print(score)