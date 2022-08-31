###
# Solution: dp
# a simple dp, note that i can be divided by j only when i > j (as unique & positive)
# so we sort the values to be a[:n], then let f(m) to be the max set size with the end of the value a[m]
# the recursive formula is f(m) = max_{i: a[m] % a[i] == 0} {f(i)} + 1
###

from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        fs = [1 for _ in range(len(nums))]
        pred_idxs = [-1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if fs[j] + 1 > fs[i]:
                        pred_idxs[i] = j
                        fs[i] = fs[j] + 1

        max_idx, max_value = 0, 1
        for i in range(1, len(nums)):
            if fs[i] > max_value:
                max_value = fs[i]
                max_idx = i

        nums_sel = []
        while max_idx >= 0:
            nums_sel.append(nums[max_idx])
            max_idx = pred_idxs[max_idx]
        return list(reversed(nums_sel))