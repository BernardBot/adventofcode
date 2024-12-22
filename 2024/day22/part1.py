import sys

sum = 0
for line in sys.stdin.read().strip().split('\n'):
    value = int(line)
    for _ in range(2000):
        value = ((value * 64) ^ value) % 16777216
        value = ((value // 32) ^ value) % 16777216
        value = ((value * 2048) ^ value) % 16777216
    sum += value
print(sum)
