import collections
import sys

graph = collections.defaultdict(set)

for line in sys.stdin.read().strip().split('\n'):
    a, b = line.split('-')
    graph[a].add(b)
    graph[b].add(a)

lan_parties = set()
for a in graph:
    if a.startswith('t'):
        for b in graph[a]:
            for c in graph[b]:
                if (
                    a in graph[b] and c in graph[b] and 
                    b in graph[a] and c in graph[a] and 
                    a in graph[c] and b in graph[c]
                ):
                    lan_parties.add(tuple(sorted((a, b, c))))
print(len(lan_parties))
