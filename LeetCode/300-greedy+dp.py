###
# Solution: greedy + dp
# O(n^2) dp is easy to  obtain, that is f(m) = max_{k: a[k] < a[m]} { f(k) } + 1
# for O(n * log n) complexity algorithm, we need to greedy hold with a increasing list, that is easiest appending increasing list;
# for example: 1, 4, 3, 7, 2, 8; from left to right the list is [1], [1, 4], [1, 3], [1, 3, 7], [1, 2, 7], [1, 2, 7, 8]
# in each time, we just conduct binary search to choose the position to replace, O(log n) each step!
###
from typing import List


class Solution:
    def binary_search(self, arr, num):
        # to find the first no less than position
        l, h = 0, len(arr) - 1
        while l < h:
            m = (l+h) >> 1
            if arr[m] < num:
                l = m + 1
            else:
                h = m - 1
        if arr[l] >= num:
            return l
        else:
            return l + 1


    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [nums[0]]
        for num in nums[1:]:
            idx = self.binary_search(arr, num)
            if idx >= len(arr):
                arr.append(num)
            else:
                arr[idx] = num
        return len(arr)

