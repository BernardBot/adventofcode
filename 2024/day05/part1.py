import collections
import sys

order, updates = sys.stdin.read().split("\n\n")

afters = collections.defaultdict(set)
for rule in order.split("\n"):
    x, y = rule.strip().split("|")
    afters[x].add(y)

def is_ordered(seq):
    s = set()
    for val in seq:
        if afters[val].intersection(s):
            return False
        s.add(val)
    return True

score = 0
for update in updates.strip().split("\n"):
    seq = update.strip().split(",")
    if is_ordered(seq):
        score += int(seq[len(seq) // 2])
print(score)
