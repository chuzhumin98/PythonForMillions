###
# Solution: priortity queue + binary search
# for the given k continuity robots, we can directly obtain its min cost,
# we just need to store a max priority queue and prefix sum, to get the min(c[i:i+M]) and sum(r[i:i+M), complexity for any k
# is O(n * log n)
# then we find that the min cost is in increasing order when k becomes larger, so that we can use binary search to
# find the k_max
###
import heapq
from typing import List

class Solution:
    def can_k_robots(self, ctimes, rtimes, target, k):
        if k == 0:
            return True
        hq = [[-num, i] for i, num in enumerate(ctimes[:k])]
        heapq.heapify(hq)
        rsum = sum(rtimes[:k])
        _maxv, _ = heapq.heappop(hq)
        heapq.heappush(hq, [_maxv, _])
        _min_sum = -_maxv + rsum * k
        for i in range(k, len(ctimes)):
            heapq.heappush(hq, [-ctimes[i], i])
            while True:
                val, idx = heapq.heappop(hq)
                if idx > i - k:
                    break
            heapq.heappush(hq, [val, idx])
            rsum += rtimes[i] - rtimes[i-k]
            _sumnow = -val + k * rsum
            _min_sum = min(_min_sum, _sumnow)
            if _min_sum <= target:
                return True
        return _min_sum <= target

    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        self.INF = 1e20
        low, high = 0, len(chargeTimes)
        # times_merge = [[chargeTimes[i], runningCosts[i]] for i in range(len(chargeTimes))]
        # times_merge.sort(key=lambda x:x[0])
        # chargeTimes = [item[0] for item in times_merge]
        # runningCosts = [item[1] for item in times_merge]
        while low < high:
            mid = (low + high) // 2
            if self.can_k_robots(chargeTimes, runningCosts, budget, mid):
                low = mid + 1
            else:
                high = mid - 1
        if self.can_k_robots(chargeTimes, runningCosts, budget, low):
            return low
        else:
            return low - 1


chargeTimes = [11,12,74,67,37,87,42,34,18,90,36,28,34,20]
runningCosts = [18,98,2,84,7,57,54,65,59,91,7,23,94,20]
budget = 937
print(Solution().maximumRobots(chargeTimes, runningCosts, budget))