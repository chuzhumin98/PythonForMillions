###
# Solution: dp
# let f(m, s, r) be the sequences number of m times rolls with ending at s (last continuely r times, r <= rollMax[s]), then
# for r = 1, f(m, s, r) = sum_{si != s, ri <= rollMax[si]} { f(m-1, si, ri) };
# for r > 1, f(m, s, r) = f(m-1, s, r-1) * I(r <= rollMax[s])
# final result is sum of f(n, ..., ...)
###
from typing import List
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = (10 ** 9) + 7
        RMAX = max(rollMax)
        fs = [[[0 for _ in range(RMAX + 1)] for __ in range(6)] for ___ in range(n)]
        for i in range(6):
            fs[0][i][1] = 1
        for i in range(1, n):
            # 1
            for cur_s in range(6):
                _sum = 0
                for k in range(6):
                    if k != cur_s:
                        for l in range(1, rollMax[k] + 1):
                            _sum = (_sum + fs[i - 1][k][l]) % MOD
                fs[i][cur_s][1] = _sum

            # > 1
            for cur_s in range(6):
                for k in range(2, rollMax[cur_s] + 1):
                    fs[i][cur_s][k] = fs[i - 1][cur_s][k - 1]

        return sum([sum(fs[-1][i]) % MOD for i in range(6)]) % MOD