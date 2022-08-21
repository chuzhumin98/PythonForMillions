def get_parent(nodes, node):
    if nodes[node] == node:
        return node
    else:
        par = nodes[node]
        root = get_parent(nodes, par)
        nodes[node] = root
        return root

def merge(nodes, nA, nB):
    parA, parB = get_parent(nodes, nA), get_parent(nodes, nB)
    if parA == parB:
        return False
    else:
        nodes[parB] = parA
        return True

n, m = input().split()
n, m = int(n), int(m)

edges = [[] for _ in range(n)]
for i in range(m):
    x, y = input().split()
    x, y = int(x), int(y)
    edges[x].append(y)
    edges[y].append(x)

k = int(input())
cuihuis = []
for i in range(k):
    cuihuis.append(int(input()))

cuihuis_set = set(cuihuis)

nodes = [i for i in range(n)]
cnt_lian = n
for node in range(n):
    if node not in cuihuis_set:
        for nodeN in edges[node]:
            if nodeN not in cuihuis_set:
                if merge(nodes, node, nodeN):
                    cnt_lian -= 1

cnt_lian -= len(cuihuis_set)
results = [cnt_lian]
for c in cuihuis[::-1]:
    cuihuis_set.remove(c)
    cnt_lian += 1
    for node in edges[c]:
        if node not in cuihuis_set:
            if merge(nodes, c, node):
                cnt_lian -= 1
    results.append(cnt_lian)

for cnt in results[::-1]:
    print(cnt)

