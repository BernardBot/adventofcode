import sys

score = 0
cmap = {}
for i, line in enumerate(sys.stdin.readlines()):
    wins, nums = line[line.index(':') + 1:].split("|")
    wins = set(wins.split())
    nums = set(nums.split())
    nwins = len(wins.intersection(nums))
    cmap[i] = cmap.get(i, 0) + 1
    for j in range(i + 1, i + nwins + 1):
        cmap[j] = cmap.get(j, 0) + cmap[i]
print(sum(cmap.values()))
