import sys

dmap = sys.stdin.read().strip()
frees = []
allocs = []
start = 0
for i in range(len(dmap)):
    size = int(dmap[i])
    if i % 2 == 0:
        allocs.append([start, size])
    else:
        frees.append([start, size])
    start += size

new_allocs = []
for a_start, a_size in reversed(allocs):
    new_allocs.append([a_start, a_size])
    for free in frees:
        f_start, f_size = free
        if f_start < a_start and f_size >= a_size:
            new_allocs[-1] = [f_start, a_size]
            free[0] += a_size
            free[1] -= a_size
            break

check = 0
for id, (start, size) in enumerate(reversed(new_allocs)):
    for i in range(start, start + size):
        check += id * i
print(check)
