###
# Solution: DSU
# a typical dsu template problem, the union requirment: si can swap no more than 1 step to obtain sj
# then we merge all possible (i, j) pair, finally to count for the connection blocks number
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

    def merge(self, nA, nB):
        parA, parB = self.get_parent(nA), self.get_parent(nB)
        self.union_set[parB] = parA

    def numSimilarGroups(self, strs: List[str]) -> int:
        self.union_set = [i for i in range(len(strs))]
        for i in range(len(strs)):
            for j in range(i):
                _delta = 0
                si, sj = strs[i], strs[j]
                for k in range(len(si)):
                    if si[k] != sj[k]:
                        _delta += 1
                        if _delta > 2:
                            break
                if _delta <= 2:
                    self.merge(j, i)
        block_set = set()
        for i in range(len(strs)):
            par = self.get_parent(i)
            if par not in block_set:
                block_set.add(par)
        return len(block_set)
