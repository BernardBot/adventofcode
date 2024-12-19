import sys

towels, patterns = sys.stdin.read().strip().split('\n\n')

towels = towels.strip().split(', ')
patterns = patterns.strip().split('\n')

score = 0
mem = {'': 1}
for pattern in patterns:
    def search(p):
        if p in mem:
            return mem[p]
        mem[p] = 0
        for towel in towels:
            if p.startswith(towel):
                count = search(p[len(towel):])
                if count > 0:
                    mem[p] += count
        return mem[p]
    score += search(pattern)

print(score)