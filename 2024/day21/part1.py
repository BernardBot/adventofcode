import collections

grid = [
    '.^A',
    '<v>',
]
width = len(grid[0])
height = len(grid)

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
symbols = '><v^'

index = {}
for x in range(width):
    for y in range(height):
        index[grid[y][x]] = (x, y)

lookup = {}
for symbol, (x, y) in index.items():
    dists = {}
    paths = collections.defaultdict(list)
    def search(x, y, path):
        if x < 0 or x >= width or y < 0 or y >= height:
            return
        if grid[y][x] == '.':
            return
        if (x, y) in dists and dists[(x, y)] < len(path):
            return
        dists[(x, y)] = len(path)
        paths[(x, y)].append(path)
        for (dx, dy), symbol in zip(moves, symbols):
            search(x + dx, y + dy, path + symbol)
    search(x, y, '')
    for (x, y), ps in paths.items():
        new_ps = []
        for p in ps:
            if len(p) == dists[(x, y)]:
                new_ps.append(p)
        paths[(x, y)] = new_ps
    lookup[symbol] = {grid[y][x]: ps for (x, y), ps in paths.items()}

# string = '<A^A>^^AvvvA'
# string = '^^^A<AvvvA>A'
"""
540A
582A
169A
593A
579A
"""

string = '<^^A<A>vvA>A' # 540A = 72
string = '<^^A^AvvAv>A' # 582A = 68
string = '^<<A^>>A^AvvvA' # 169A = 76
string = '<^^A>^AvvAvA' # 593A = 74
string = '<^^A<^A>>AvvvA' # 579A = 72

print(540 * 72 + 582 * 68 + 169 * 76 + 593 * 74 + 579 * 72)

def integ(string):
    fr = 'A'
    results = ['']
    for to in string:
        new_results = []
        for result in results:
            for new in lookup[fr][to]:
                new_result = result + new + 'A'
                new_results.append(new_result)
        fr = to
        results = new_results
    return results


min_len = 1000000
r = integ(string)
for string in r:
    intg = integ(string)
    for r2 in intg:
        min_len = min(min_len, len(r2))
print(min_len)