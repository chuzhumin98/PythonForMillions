###
# Solution: monotonic stack
# we can hold for a monotonic increasing stack, to record for each node, which is the longest interval when
# the smallest value equals to this node (the front stack node idx + 1 to current pop it index - 1).
# then we just need to check including k intervals, to find for the max value
###

from typing import List
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        stack = [[0, -1]]
        _max_value = 0
        for i, num in enumerate(nums):
            while stack[-1][0] >= num:
                if stack[-2][1] + 1 <= k and k <= i - 1:
                    _max_value = max(_max_value, (i - stack[-2][1] - 1) * stack[-1][0])
                stack.pop()
            stack.append([num, i])

        while len(stack) > 1:
            if stack[-2][1] + 1 <= k:
                _max_value = max(_max_value, (len(nums) - stack[-2][1] - 1) * stack[-1][0])
            stack.pop()
        return _max_value

