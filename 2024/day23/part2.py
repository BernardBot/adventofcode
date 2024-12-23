import collections
import sys

graph = collections.defaultdict(set)

for line in sys.stdin.read().strip().split('\n'):
    a, b = line.split('-')
    graph[a].add(b)
    graph[b].add(a)


for a in graph:
    graph[a].add(a)

results = []
for a in graph:
    cluster = set(graph[a])
    for b in graph[a]:
        if b not in cluster:
            continue
        new_cluster = cluster.intersection(graph[b])
        if len(new_cluster) < len(cluster) - 1:
            cluster.remove(b)
        else:
            cluster = new_cluster
    results.append(','.join(sorted(list(cluster))))

result = sorted(results, key=lambda x: len(x))[-1]
print(result)
