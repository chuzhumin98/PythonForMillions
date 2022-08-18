from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums_nonzero = [num for num in nums if num > 0]
        cnt = 0
        while True:
            if len(nums_nonzero) == 0:
                break
            min_value = min(nums_nonzero)
            nums_new = [num-min_value for num in nums_nonzero]
            nums_nonzero = [num for num in nums_new if num > 0]
            cnt += 1
        return cnt