import sys

score = 0
lines =  sys.stdin.readlines()
for i in range(0, len(lines), 3):
    common = set(lines[i].strip())
    for j in range(1, 3):
        common = common.intersection(set(lines[i + j].strip()))
    for item in common:
        if 'a' <= item and item <= 'z':
            score += ord(item) - ord('a') + 1
        else:
            score += ord(item) - ord('A') + 27
print(score)