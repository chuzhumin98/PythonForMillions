###
# Solution: dfs
# you can refer the link https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/solution/by-affine-9og3/ to see the specific solution of mine
###
from typing import List
class Solution:
    def dfs(self, rms, cur_idx):
        if self.can_do:
            return
        if cur_idx == self.n:
            if max(rms) == 0:
                self.can_do = True
            return
        aset = set()
        val = self.nums[cur_idx]
        for i, num in enumerate(rms):
            if val <= num:
                if num not in aset:
                    aset.add(num)
                    rms[i] -= val
                    self.dfs(rms, cur_idx + 1)
                    rms[i] += val

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)
        _sum = sum(nums)
        if _sum % k != 0:
            return False
        else:
            val = _sum // k
            if nums[0] > val:
                return False
            sidx = 0
            self.n = len(nums)
            while sidx < self.n:
                if nums[sidx] == val:
                    sidx += 1
                    k -= 1
                else:
                    break

            if k == 0:
                return True

            self.nums = nums
            self.can_do = False
            rms = [val for _ in range(k)]
            self.dfs(rms, sidx)
            return self.can_do
