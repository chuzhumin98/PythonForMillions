###
# Solution: DSU (disjoint set union) + Tree-like Array
# we think this problem from the end to start, each time add one number a_i to the array idx i, that is make connection between array idx i with i-1 and
# i with i+1, we can use dsu to store each connection block's left and right end
# then we use a tree-like array to store for the prefix sum of current array, so as to calculate for each time's adding interval's sum
###

from typing import List
class Solution:
    def get_parent_left(self, node):
        if self.set_left[node] == node:
            return node
        else:
            par = self.set_left[node]
            root = self.get_parent_left(par)
            self.set_left[node] = root
            return root

    def get_parent_right(self, node):
        if self.set_right[node] == node:
            return node
        else:
            par = self.set_right[node]
            root = self.get_parent_right(par)
            self.set_right[node] = root
            return root

    def merge_left(self, nA, nB):
        rootA, rootB = self.get_parent_left(nA), self.get_parent_left(nB)
        self.set_left[rootB] = rootA

    def merge_right(self, nA, nB):
        rootA, rootB = self.get_parent_right(nA), self.get_parent_right(nB)
        self.set_right[rootB] = rootA

    def lowbit(self, num):
        return num & (-num)

    def get_tree_prefixsum(self, idx):
        _sum = 0
        while idx > 0:
            _sum += self.tree_list[idx]
            idx -= self.lowbit(idx)
        return _sum

    def set_tree_num(self, idx, num):
        while idx <= self.N:
            self.tree_list[idx] += num
            idx += self.lowbit(idx)

    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        self.N = len(nums)
        self.set_left = [i for i in range(self.N)]
        self.set_right = [i for i in range(self.N)]
        _max_cur = 0
        max_list = [0]

        self.tree_list = [0 for i in range(self.N + 1)]
        nums_huifu = [False for i in range(self.N + 2)]
        for idx in removeQueries[::-1]:
            num = nums[idx]
            nums_huifu[idx + 1] = True
            self.set_tree_num(idx + 1, num)
            if nums_huifu[idx]:
                self.merge_left(idx - 1, idx)
                self.merge_right(idx, idx - 1)
            if nums_huifu[idx + 2]:
                self.merge_right(idx + 1, idx)
                self.merge_left(idx, idx + 1)
            low, high = self.get_parent_left(idx), self.get_parent_right(idx)
            _sum = self.get_tree_prefixsum(high + 1) - self.get_tree_prefixsum(low)
            _max_cur = max(_max_cur, _sum)
            max_list.append(_max_cur)
            # print(_sum, _sum_max)
            # print(self.set_left)
            # print(self.set_right)
            # print(self.tree_list)
        return list(reversed(max_list[:self.N]))

if __name__ == '__main__':
    nums = [1, 2, 5, 6, 1]
    removeQueries = [0, 3, 2, 4, 1]
    print(Solution().maximumSegmentSum(nums, removeQueries))