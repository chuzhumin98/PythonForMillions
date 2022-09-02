###
# Solution: Priority Queue + HashSet
# first we push 1 into priority queue, for each pop value (v) from pq, that is just the k-th min value (k-th pop step),
# then we put v*p (for each p in primes) into pq if it has not be put into pq (use a hashset to store this info)
###

from typing import List
import heapq


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        aset = set([1])
        hq = [1]
        heapq.heapify(hq)
        num = None
        for i in range(n):
            num = heapq.heappop(hq)
            for prime in primes:
                val = num * prime
                if val not in aset:
                    aset.add(val)
                    heapq.heappush(hq, val)
        return num

