###
# Solution: Tree DP
# a typical tree dp problem, for each node, we hold lmax(node), rmax(node) to be the max length of its left / right subtree (must can link to node itself)
# then, lmax(node) = max{ lmax(node.left), rmax(node.left) } + 1 if node.left.val = node.val else 0
# rmax(node) = max{ lmax(node.right), rmax(node.right) } + 1 if node.right.val = node.right else 0
# then max_node { lmax(node) + rmax(node) } is the answer
###

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, node):
        node.lmax = 0
        node.rmax = 0
        if node.left:
            self.dfs(node.left)
            if node.val == node.left.val:
                node.lmax = max(node.left.lmax, node.left.rmax) + 1
        if node.right:
            self.dfs(node.right)
            if node.val == node.right.val:
                node.rmax = max(node.right.lmax, node.right.rmax) + 1
        self.total_max = max(self.total_max, node.lmax + node.rmax)
        # print(f'val = {node.val}, lmax = {node.lmax}, rmax = {node.rmax}')

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.total_max = 0
        self.dfs(root)
        return self.total_max

