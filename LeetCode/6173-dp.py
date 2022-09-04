###
# Solution: dp with state compression
# we consider the opposite problem, how to choose K column to make the row contains 1 minimum
# let f(S, k) represents if we can select k column to reach the 1 state to be S (a binary base representation,
# for example, 01001 denotes the second-row and fifth-row contains 1, but another three rows donot.
# then in the t-th iteration (t is the column number, s_t is the t-th column's state representation),
# f(S|s_t, k) is true if f(S, k-1) or f(S|s_t, k) is true
###

from typing import List
class Solution:
    def lowbit(self, n):
        return n & (-n)

    def one_nums(self, n):
        _sum = 0
        while n > 0:
            n -= self.lowbit(n)
            _sum += 1
        return _sum


    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        m, n = len(mat), len(mat[0])
        k = n - cols
        SSIZE = 1 << m
        fs = [[False for _ in range(k+1)] for __ in range(SSIZE)]
        fs[0][0] = True
        statuss = []
        for j in range(n):
            _status = 0
            for i in range(m):
                _status = _status * 2 + mat[i][j]
            statuss.append(_status)

        for _status in statuss:
            for j in range(k-1, -1, -1):
                for i in range(SSIZE):
                    if fs[i][j]:
                        fs[i | _status][j+1] = True

        min_ones = m
        for i in range(SSIZE):
            if fs[i][k]:
                min_ones = min(min_ones, self.one_nums(i))
        return m - min_ones

mat = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]]
cols = 2
print(Solution().maximumRows(mat, cols))