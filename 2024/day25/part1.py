import sys

locks = set()
keys = set()

for string in sys.stdin.read().strip().split('\n\n'):
    if string.startswith('#####'):
        lock = [0] * 5
        for i, line in enumerate(string.split('\n')[1:]):
            for j, c in enumerate(line):
                if c == '#':
                    lock[j] = max(i + 1, lock[j])
        locks.add(tuple(lock))
    else:
        key = [0] * 5
        for i, line in enumerate(string.split('\n')[::-1][1:]):
            for j, c in enumerate(line):
                if c == '#':
                    key[j] = max(i + 1, key[j])
        keys.add(tuple(key))

combos = set()
for lock in locks:
    for key in keys:
        fits = True
        for x, y in zip(lock, key):
            if x + y > 5:
                fits = False
                break
        if fits:
            combos.add((lock ,key))
print(len(combos))
