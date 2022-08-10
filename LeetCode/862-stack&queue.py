###
# Solution: Monotonic bidirectional queue
# we hold a monotonic increase bidirectional queue for the prefix sum of nums,
# if the inserting value v - queue[0] >= k, then pop the queue front value until the delta less than k, also considering any no less than pair (queue[0], v);
# if v <= queue[-1], then pop the queue end value until v > queue[-1] or queue is empty
###

import collections
from typing import List

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        suffix_sum = [nums[0]]
        for i in range(1, len(nums)):
            suffix_sum.append(suffix_sum[-1] + nums[i])

        minLen = 1 << 30

        queue = collections.deque()
        queue.append([0, -1])  # sum, idx
        for i, _sum in enumerate(suffix_sum):
            while True:
                if len(queue) == 0:
                    break
                if _sum - queue[0][0] >= k:
                    minLen = min(minLen, i - queue[0][1])
                    queue.popleft()
                else:
                    break

            if len(queue) > 0 and queue[-1][0] >= _sum:
                while True:
                    if len(queue) == 0:
                        break
                    if queue[-1][0] >= _sum:
                        queue.pop()
                    else:
                        break

            queue.append([_sum, i])

        if minLen == 1 << 30:
            return -1
        else:
            return minLen

if __name__ == '__main__':
    print(Solution().shortestSubarray([2, -1, 2], 3))