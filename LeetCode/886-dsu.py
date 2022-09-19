###
# Solution: dsu
# We just need to hold with a dsu, for each node, we not only record its parent, as well as its relation with parent
# for each dislike relation, we just need to merge these two people with dislike
# relation, before merge, we need to check if it is contradictory with previous relations
###
from typing import List
class Solution:
    def get_parent(self, node):
        if self.union_set[node][0] == node:
            return self.union_set[node]
        else:
            par, rel1 = self.union_set[node]
            root, rel2 = self.get_parent(par)
            rt = (rel1 + rel2) % 2
            self.union_set[node] = [root, rt]
            return root, rt

    def merge(self, nodeA, nodeB):
        rootA, relA = self.get_parent(nodeA)
        rootB, relB = self.get_parent(nodeB)
        if rootA == rootB:
            return (relA + relB) % 2 == 1
        else:
            self.union_set[rootB] = [rootA, (relA + relB + 1) % 2]
            return True

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        self.union_set = [[i, 0] for i in range(n + 1)]
        for ai, bi in dislikes:
            if not self.merge(ai, bi):
                return False
        return True
