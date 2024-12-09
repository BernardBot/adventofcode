import sys

dmap = sys.stdin.read().strip()
mem = []
for i in range(len(dmap)):
    size = int(dmap[i])
    val = i // 2 if i % 2 == 0 else '.'
    for j in range(size):
        mem.append(val)
i = 0
j = len(mem) - 1
while True:
    while mem[i] != '.':
        i += 1
    if i > j:
        break
    while mem[i] == '.' and mem[j] != '.':
        mem[i] = mem[j]
        mem[j] = '.'
        i += 1
        j -= 1
    while mem[j] == '.':
        j -= 1

check = 0
for x in range(i):
    check += x * mem[x]
print(check)