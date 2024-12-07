lines = open("inputa.txt").readlines()

graph = {}

for line in lines:
    fr, to = line.strip().split("-")

    if fr not in graph:
        graph[fr] = set([to])
    else:
        graph[fr].add(to)

    if to not in graph:
        graph[to] = set([fr])
    else:
        graph[to].add(fr)

visited = set()
cur = []
paths = []

def dfs(u, v):
    if u.islower() and u in visited:
        return

    visited.add(u)
    cur.append(u)

    if u == v:
        paths.append(cur[:])
        visited.remove(u)
        cur.pop()
        return

    if u in graph:
        for w in graph[u]:
            dfs(w, v)
    
    if u in visited:
        visited.remove(u)
    cur.pop()

dfs("start", "end")
print(len(paths))