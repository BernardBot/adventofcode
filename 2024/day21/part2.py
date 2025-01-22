# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
# These are hardcoded for our input,
# you could make this more general with a shortest path
# algorithm. The same could be done for the keypad.
num_paths = {
    'A5': ['^^<', '<^^', '^<^'],
    '54': ['<'],
    '40': ['>vv', 'v>v'],
    '0A': ['>'],

    '58': ['^'],
    '82': ['vv'],
    '2A': ['>v', 'v>'],

    'A1': ['^<<', '<^<'],
    '16': ['^>>', '>>^'],
    '69': ['^'],
    '9A': ['vvv'],

    '59': ['^>', '>^'],
    '93': ['vv'],
    '3A': ['v'],

    '57': ['<^', '^<'],
    '79': ['>>'],
}

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
paths = {
    '<<': [''],
    '<>': ['>>'],
    '<A': ['>>^','>^>'],
    '<^': ['>^'],
    '<v': ['>'],

    '><': ['<<'],
    '>>': [''],
    '>A': ['^'],
    '>^': ['<^', '^<'],
    '>v': ['<'],

    'A<': ['v<<', '<v<'],
    'A>': ['v'],
    'AA': [''],
    'A^': ['<'],
    'Av': ['<v', 'v<'],

    '^<': ['v<'],
    '^>': ['<v', 'v>'],
    '^A': ['>'],
    '^^': [''],
    '^v': ['v'],

    'v<': ['<'],
    'v>': ['>'],
    'vA': ['>^','^>'],
    'v^': ['^'],
    'vv': [''],
}

def from_num(sub):
    results = [[]]
    cur = 'A'
    for nxt in sub:
        new_results = []
        for p in num_paths[cur + nxt]:
            for result in results:
                new_results.append(result + [p + 'A'])
        results = new_results
        cur = nxt
    return results

mem = {}
def search_sub(sub, depth):
    if depth == 0:
        return len(sub)

    if (sub, depth) not in mem:
        cur = 'A'
        total = 0
        for nxt in sub:
            total += min(search_sub(p + 'A', depth - 1) for p in paths[cur + nxt])
            cur = nxt
        mem[(sub, depth)] = total

    return mem[(sub, depth)]

def search(seq, depth):
    total = 0
    for sub in seq:
        total += search_sub(sub, depth)
    return total

total = 0
for line in open('input').readlines():
    line = line.strip()
    val = int(line[:-1])
    result = float('inf')
    for seq in from_num(line):
        new_result = search(seq, 25)
        result = min(result, new_result)
    total += val * result
print(total)
