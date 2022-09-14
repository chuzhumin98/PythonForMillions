from typing import List
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minv = nums[0]
        maxv = -(1 << 31)
        for num in nums[1:]:
            maxv = max(maxv, num - minv)
            minv = min(num, minv)

        return maxv if maxv > 0 else -1