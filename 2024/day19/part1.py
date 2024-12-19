import sys

towels, patterns = sys.stdin.read().strip().split('\n\n')

towels = towels.strip().split(', ')
patterns = patterns.strip().split('\n')

score = 0
mem = {}
for pattern in patterns:
    def search(p):
        if p == '':
            return True
        if p in mem:
            return mem[p]
        for towel in towels:
            if p.startswith(towel):
                if search(p[len(towel):]):
                    mem[p] = True
                    return True
        mem[p] = False
        return False
    score += search(pattern)

print(score)