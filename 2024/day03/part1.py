import re
import sys

input = sys.stdin.read()
r = re.compile(r'mul\(\d+,\d+\)')

sum = 0
for mul in r.findall(input):
    x, y = mul[4:-1].split(",")
    sum += int(x) * int(y)

print(sum)
