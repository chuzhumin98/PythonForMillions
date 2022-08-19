from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def arg_max(self, nums, low, high):
        maxV, maxI = nums[low], low
        for i in range(low+1, high+1):
            if nums[i] > maxV:
                maxV = nums[i]
                maxI = i
        return maxI

    def constructNode(self, nums, low, high):
        maxI = self.arg_max(nums, low, high)
        node = TreeNode(nums[maxI])
        if maxI - low > 0:
            leftnode = self.constructNode(nums, low, maxI-1)
            node.left = leftnode
        if high - maxI > 0:
            rightnode = self.constructNode(nums, maxI+1, high)
            node.right = rightnode
        return node

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.constructNode(nums, 0, len(nums)-1)