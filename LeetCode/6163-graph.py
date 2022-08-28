###
# Solution: graph + Toposort
# a typical toposort template problem, we need to conduct toposort on both row and column direction, if the both sort is valid,
# then the constraints can be satisfied, else then cannot all be satisfied
###

from typing import List
class Solution:
    def toposort(self, conds, k):
        edges = [set() for _ in range(k)]
        inds = [0 for _ in range(k)]
        nonused = set([i for i in range(k)])
        for ai, bi in conds:
            if (bi - 1) not in edges[ai - 1]:
                edges[ai - 1].add(bi - 1)
                inds[bi - 1] += 1
        arr_sort = []
        while True:
            if len(nonused) == 0:
                break
            sidx = -1
            for idx in nonused:
                if inds[idx] == 0:
                    sidx = idx
                    break
            if sidx == -1:
                return False, arr_sort
            else:
                arr_sort.append(sidx)
                for idx in edges[sidx]:
                    inds[idx] -= 1
                nonused.remove(sidx)
        return True, arr_sort

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        flagR, arr_R = self.toposort(rowConditions, k)
        flagC, arr_C = self.toposort(colConditions, k)
        posiR, posiC = [0 for _ in range(k)], [0 for _ in range(k)]
        for i, n in enumerate(arr_R):
            posiR[n] = i
        for i, n in enumerate(arr_C):
            posiC[n] = i
        if not flagR or not flagC:
            return []
        else:
            matrix = [[0 for _ in range(k)] for __ in range(k)]
            for i in range(k):
                r, c = posiR[i], posiC[i]
                matrix[r][c] = i + 1
            return matrix
