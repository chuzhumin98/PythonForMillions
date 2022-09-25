###
# Solution: DSU
# we order the vals with increasing order, each time, when we consider the nodes with val = v,
# we add all edges of them linking with a vertex valued no more than value v, we just to record each nodes with val = v's
# belonged connection block, for each block b, it offers the count with C(b,2)+b
###
from typing import List
class Solution:
    def get_parent(self, node):
        if self.union_set[node] == node:
            return node
        else:
            par = self.union_set[node]
            root = self.get_parent(par)
            self.union_set[node] = root
            return root

    def merge(self, nodeA, nodeB):
        rA, rB = self.get_parent(nodeA), self.get_parent(nodeB)
        self.union_set[rB] = rA

    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        self.union_set = [i for i in range(n)]
        vals_dict = dict()
        for i, val in enumerate(vals):
            if val not in vals_dict:
                vals_dict[val] = [i]
            else:
                vals_dict[val].append(i)
        vals_dict_items = sorted(vals_dict.items(), key=lambda x:x[0])
        edges_pv = [[] for _ in range(n)]
        for a, b in edges:
            edges_pv[a].append(b)
            edges_pv[b].append(a)
        _sum = 0
        for val, idxs in vals_dict_items:
            for idx in idxs:
                for b in edges_pv[idx]:
                    if vals[b] <= val:
                        self.merge(idx, b)
            pars = dict()
            for idx in idxs:
                root = self.get_parent(idx)
                pars[root] = pars.get(root, 0) + 1

            for root in pars:
                cnt = pars[root]
                _sum += cnt + cnt * (cnt-1) // 2
        return _sum

vals = [1,3,2,1,3]
edges = [[0,1],[0,2],[2,3],[2,4]]
print(Solution().numberOfGoodPaths(vals, edges))
