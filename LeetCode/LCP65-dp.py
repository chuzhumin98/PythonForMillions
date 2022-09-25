###
# Solution: dp
# let f(n, d) be the min value of interval (max and min of prefix sum) for a[1:n] when cur prefixsum is d + min value
# note that f(n, d) >= d for definition
# then f(n+1, d + a[n+1]) = max(f(n, d), d + a[n+1])  (to choose + num);
# if d >= a[n+1], f(n+1, d - a[n+1]) = f(n, d); if d < a[n+1], f(n+1, 0) = f(n, d) + a[n+1] - d
# note that the answer must be no more than 2000, so that we just need to consider d <= 2000, if d > 2000, directly drop it!
# thus, the complextity is O(N * 2000)
###
from typing import List

class Solution:
    def unSuitability(self, operate: List[int]) -> int:
        INF = 1 << 31
        NMAX = 2001
        fs_pred = [INF for _ in range(NMAX)]
        fs_pred[0] = operate[0]
        for num in operate[1:]:
            fs = [INF for _ in range(NMAX)]
            for d, minv in enumerate(fs_pred):
                if minv == INF:
                    continue
                val = num + d
                minv_this = max(minv, val)
                if minv_this < NMAX:
                    fs[val] = min(fs[val], minv_this)

                val = d - num
                if val >= 0:
                    fs[val] = min(fs[val], minv)
                else:
                    fs[0] = min(fs[0], minv - val)
            fs_pred = fs
        return min(fs_pred)

