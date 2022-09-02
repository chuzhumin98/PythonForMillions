###
# Solution: dp
# a simple dp, optimal substatus is (position, remain fuel), let f(m, n) be the path number with remain fuel n at l[m] (location)
# then f(m, n) = \sum_{k} f(k, n + |l[m]-l[k]|)
###

from typing import List


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        P = 1000000007
        INF = 1 << 30
        n = len(locations)
        fs = [[0 for _ in range(fuel + 1)] for __ in range(n)]
        fs[start][fuel] = 1
        dists = [[0 for _ in range(n)] for __ in range(n)]
        for i in range(n):
            for j in range(n):
                dists[i][j] = abs(locations[i] - locations[j])
            dists[i][i] = INF
        for f in range(fuel-1, -1, -1):
            for l in range(n):
                _sum = 0
                for ll in range(n):
                    val = f + dists[l][ll]
                    _sum += fs[ll][val] if val <= fuel else 0
                fs[l][f] = _sum % P
        return sum([fs[finish][i] for i in range(fuel+1)]) % P