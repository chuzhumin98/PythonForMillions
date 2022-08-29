###
# Solution: BFS
# note that for each cycle (a1, a2), (a2, a3), ... (ak, a1), we can use (k-1) swaps to make all cp together
# then, we can just use one BFS process to calculate the cycle number, the answer is just n - {cycle number}
###

from typing import List
import collections
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        _block = 0
        n = len(row) // 2
        edges = [[] for _ in range(n)]
        for i in range(n):
            idx1, idx2 = row[i*2], row[i*2+1]
            g1, g2 = idx1 // 2, idx2 // 2
            edges[g1].append(g2)
            edges[g2].append(g1)
        used = [False for _ in range(n)]
        for i in range(n):
            if not used[i]:
                dq = collections.deque()
                dq.append(i)
                used[i] = True
                _block += 1
                while len(dq) > 0:
                    idx = dq.popleft()
                    for e in edges[idx]:
                        if not used[e]:
                            used[e] = True
                            dq.append(e)
        return n - _block
