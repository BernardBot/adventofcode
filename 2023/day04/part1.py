import sys

score = 0
for line in sys.stdin.readlines():
    wins, nums = line[line.index(':') + 1:].split("|")
    wins = set(wins.split())
    nums = set(nums.split())
    wnums = wins.intersection(nums)
    if wnums:
        score += 2 ** (len(wnums) - 1)
print(score)
