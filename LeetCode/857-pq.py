###
# Solution: Priority Queue
# we find two factors affect the selectness of each work: ratio of wage/quality, quality
# the final total wage = max(ratio of wage/quality selected) * sum(quality selected)
# thus, we can sort with the ratio of wage/quality, each time, we push one larger ratio work into the pq,
# also pop the max(quality) one, to calculate for each select choice's total wage, to find the min value
###
from typing import List
import heapq
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = [[wage[i]/float(quality[i]), i] for i in range(len(quality))]

        workers.sort(key=lambda x:x[0])
        hq = []
        _sum_qual, ratio = 0, 0
        for i in range(k):
            ratio, idx = workers[i]
            _sum_qual += quality[idx]
            hq.append(-quality[idx])
        heapq.heapify(hq)

        minv = _sum_qual * ratio

        for ratio, idx in workers[k:]:
            qual = quality[idx]
            heapq.heappush(hq, -qual)
            qual_out = -heapq.heappop(hq)
            _sum_qual += qual - qual_out
            minv = min(minv, _sum_qual * ratio)
        return minv