import sys

score = 0
for line in sys.stdin.readlines():
    line = line.strip()
    left = line[:(len(line) // 2)]
    rigt = line[len(line) // 2:]
    common = set(left).intersection(set(rigt))
    for item in common:
        if 'a' <= item and item <= 'z':
            score += ord(item) - ord('a') + 1
        else:
            score += ord(item) - ord('A') + 27
print(score)