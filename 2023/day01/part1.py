import sys

score = 0
for line in sys.stdin.readlines():
    first = None
    for char in line.strip():
        if char in '123456789':
            if first is None:
                first = char
            last = char
    score += int(first + last)
print(score)