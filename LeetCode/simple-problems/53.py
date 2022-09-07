from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxv = nums[0]
        _sum = 0
        for num in nums:
            _sum += num
            maxv = max(maxv, _sum)
            _sum = max(_sum, 0)
        return maxv