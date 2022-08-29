###
# Solution: dp
# we consider the first split to construct optimal sub-structure,
# let f(m, n) to be the max price to earn for a (m, n) hood, then
# considering all possible split: each row and each column, then
# f(m, n) = max {max_k(f(k, n) + f(m-k, n), max_k(f(m, k) + f(m, n-k)), I(price if (m, n) is one kind of wood)}
###

from typing import List

class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        fs = [[0 for _ in range(n + 1)] for __ in range(m + 1)]
        for h, w, price in prices:
            if h <= m and w <= n:
                fs[h][w] = price  # one possible selection, no guarantee max
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for spR in range(1, 1 + (i + 1) // 2):
                    fs[i][j] = max(fs[i][j], fs[spR][j] + fs[i - spR][j])
                for spC in range(1, 1 + (j + 1) // 2):
                    fs[i][j] = max(fs[i][j], fs[i][spC] + fs[i][j - spC])
        return fs[m][n]
