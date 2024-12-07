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

def make_ordered(seq):
    new_seq = seq[:]
    s = set()
    i = 0
    while i < len(seq):
        val = seq[i]
        sec = afters[val].intersection(s)
        if not sec:
            s.add(val)
            i += 1
            continue
        new_index = min(new_seq.index(val2) for val2 in sec)
        new_seq.remove(val)
        new_seq.insert(new_index, val)
        s.add(val)
        i += 1
    return new_seq

score = 0
for update in updates.strip().split("\n"):
    seq = update.strip().split(",")
    if is_ordered(seq):
        continue
    new_seq = make_ordered(seq)
    print(new_seq)
    score += int(new_seq[len(new_seq) // 2])
print(score)
