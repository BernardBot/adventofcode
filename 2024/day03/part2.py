import re
import sys

input = sys.stdin.read()
r = re.compile(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)')

sum = 0
enabled = True
for op in r.findall(input):
    if op == 'do()':
        enabled = True
    elif op == "don't()":
        enabled = False
    elif enabled:
        x, y = op[4:-1].split(",")
        sum += int(x) * int(y)

print(sum)
