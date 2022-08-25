###
# Solution: Graph, Topo Sort
# we use topo sort to deal with this problem, that is
# determined: in each time only one node is indegree = 0, uniquely determine the sorted list;
# contradition: exist ring in the graph, in one time all of each non-use node is indegree > 0
# non-determined: even with the last relation, there exist one time, no more than one non-use node indegree = 0
# caution!!!usually mistake!!! when non-determined, we also need to finish the whole process of topo sort to check if contraditary
###

import copy
def get_topo_result(edges, indegrees):
    remain_nodes = [key for key in edges]
    remain_nodes = set(remain_nodes)
    uniqued = True
    sort_list = []
    while True:
        if len(remain_nodes) == 0:
            if uniqued:
                return 1, sort_list # succeed
            else:
                return 0, sort_list # non-determine
        cnt_noin, idx_noin = 0, -1
        for node in remain_nodes:
            if indegrees[node] == 0:
                cnt_noin += 1
                idx_noin = node
        if cnt_noin == 0:
            return 2, sort_list # cycled
        elif cnt_noin > 1:
            uniqued = False # no determined
        sort_list.append(idx_noin)
        for outnode in edges[idx_noin]:
            indegrees[outnode] -= 1
        remain_nodes.remove(idx_noin)

n, m = input().split()
n, m = int(n), int(m)
edges = dict()
indegrees = dict()

relations = []
for i in range(m):
    relations.append(input().strip())

type = 0
for i, relation in enumerate(relations):
    a, b = relation.split('<')
    if a not in edges:
        edges[a] = set()
        indegrees[a] = 0
    if b not in edges:
        edges[b] = set()
        indegrees[b] = 0
    if b not in edges[a]:
        indegrees[b] += 1
        edges[a].add(b)

    type, sort_list = get_topo_result(edges, copy.deepcopy(indegrees))
    if type == 1:
        if len(edges) == n:
            print(f'Sorted sequence determined after {i+1} relations: {"".join(sort_list)}.')
            break
        else:
            type = 0
    elif type == 2:
        print(f'Inconsistency found after {i+1} relations.')
        break

if type == 0:
    print('Sorted sequence cannot be determined.')




