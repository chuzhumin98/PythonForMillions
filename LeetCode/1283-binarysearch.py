###
# Solution: Binary Search
# a simple binary search, we need to use binary search to find the answer
###

from typing import List


class Solution:
    def check(self, nums, target, k):
        _sum = 0
        for num in nums:
            _sum += (num + k - 1) // k
        return _sum <= target

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low, high = 1, max(nums)
        while low < high:
            mid = (low + high) // 2
            if self.check(nums, threshold, mid):
                high = mid - 1
            else:
                low = mid + 1
        if self.check(nums, threshold, low):
            return low
        else:
            return low + 1