###
# Solution: DSU
# we use DSU to obtain each connection blocks in the nodes set,
# for each connection blocks, the result is the number of co-occurance values
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
        parA, parB = self.get_parent(nodeA), self.get_parent(nodeB)
        self.union_set[parB] = parA

    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        self.union_set = [_ for _ in range(len(source))]
        for a, b in allowedSwaps:
            self.merge(a, b)

        groups = dict()
        for i in range(len(source)):
            par = self.get_parent(i)
            if par not in groups:
                groups[par] = [i]
            else:
                groups[par].append(i)

        _sum = 0
        for key in groups:
            group = groups[key]
            cnts = dict()
            for idx in group:
                cnts[source[idx]] = cnts.get(source[idx], 0) + 1
            for idx in group:
                if cnts.get(target[idx], 0) >= 1:
                    cnts[target[idx]] -= 1
                    _sum += 1
        return len(source) - _sum

