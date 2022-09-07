from typing import List
import collections
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        INF = 2147483647
        min_single_history = INF
        minv = INF

        dq = collections.deque() # now is useless as the right end is larger than concerned idx

        sidx = 0
        _sum = 0
        for i, num in enumerate(arr):
            _sum += num
            while _sum > target:
                _sum -= arr[sidx]
                sidx += 1
            if _sum == target:
                while len(dq) > 0:
                    if dq[0][1] < sidx: # [len, eidx]
                        l, edix = dq.popleft()
                        min_single_history = min(min_single_history, l)
                    else:
                        break
                len_this = i - sidx + 1
                minv = min(minv, min_single_history + len_this)
                dq.append([len_this, i])
        if minv == INF:
            return -1
        else:
            return minv