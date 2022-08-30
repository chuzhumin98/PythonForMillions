###
# Solution: priority queue
# we first sort the left end and right end of intervals, each query in increasing order.
# then we need to hold a data structure to support the following operation:
# 1. insert a value r - l + 1 (left end of interval)
# 2. delete a value r - l + 1 (right end of interval)
# 3. query the min value
# obviously, priority queue can satisfy these requirements in O(log n) complexity (with lazy delete)
###

import heapq
from typing import List
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        events = []
        for l, r in intervals:
            events.append([l, 0, r - l + 1, r])  # type: 0-insert, 1-query
        for idx, q in enumerate(queries):
            events.append([q, 1, r - l + 1, idx])

        _ans = [-1 for _ in range(len(queries))]
        hq = []
        heapq.heapify(hq)
        events.sort(key=lambda x: x[0] + 0.1 * x[1])
        for e in events:
            idx, ty, val, ridx = e
            if ty == 0:
                heapq.heappush(hq, [val, ridx])
            elif ty == 1:
                while len(hq) > 0:
                    val, r = heapq.heappop(hq)
                    if r >= idx:
                        heapq.heappush(hq, [val, r])
                        _ans[ridx] = val
                        break
                    else:
                        pass
        return _ans