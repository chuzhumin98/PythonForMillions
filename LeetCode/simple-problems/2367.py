from typing import List
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        nums_set = set(nums)
        _sum = 0
        for num in nums:
            if num + diff in nums_set and num + diff * 2 in nums_set:
                _sum += 1
        return _sum