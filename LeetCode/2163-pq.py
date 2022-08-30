###
# Solution: priority queue
# note that the nums[:n] must be in the candidates set of first array, nums[2n:3n] must be in the candidates set of second array
# the freedom is how to split the medium nums[n:2n] number, into first array or second array candiates?
# thus, we just need to all possible n+1 choices, for the first array and second array, we need to choose the top-n smallest (or
# largest) number in these n~2n numbers.
# to online reuse the pred information, when we iter from n to 2n (index i), we need to add it to a[:i] max heap, pop the largest value;
# also, we need to check if it is in the a[i:] min heap, when it locates in, we need to delete it and choose one a[j] (j > i),
# the largest value of the dropped value from a[i:] min heap, put it into the a[i:] min heap, to fill with the blank
# position of the poped a[i]
###

from typing import List
import heapq

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        hq_left, hq_right, hq_right_cdd = [], [], []
        heapq.heapify(hq_left)
        heapq.heapify(hq_right)
        heapq.heapify(hq_right_cdd)
        inheap = [True for _ in range(n)]  # to store if nums[n+_] is or not in hq_right
        _sum_left, _sum_right = 0, 0
        for num in nums[:n]:
            heapq.heappush(hq_left, -num)
            _sum_left += num

        for i in range(n, n * 2):
            num = nums[i]
            heapq.heappush(hq_right, [num, i])
            _sum_right += num
        for i in range(n * 2, n * 3):
            num = nums[i]
            heapq.heappush(hq_right, [num, i])
            num_rm, ridx = heapq.heappop(hq_right)
            heapq.heappush(hq_right_cdd, [-num_rm, ridx])
            if ridx < n * 2:
                inheap[ridx - n] = False
            _sum_right += num - num_rm

        min_delta = _sum_left - _sum_right
        for i in range(n):
            num = nums[n + i]
            heapq.heappush(hq_left, -num)
            num_rm = -heapq.heappop(hq_left)
            _sum_left += num - num_rm

            if inheap[i]:
                while True:
                    num_sel, sidx = heapq.heappop(hq_right_cdd)
                    num_sel = -num_sel
                    if sidx - n > i:
                        break
                _sum_right += num_sel - num
                if sidx < n * 2:
                    inheap[sidx - n] = True

            min_delta = min(min_delta, _sum_left - _sum_right)
            # print(f"i = {i}, sum_left = {_sum_left}, sum_right = {_sum_right}")
        return min_delta




