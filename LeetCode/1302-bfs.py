###
# Solution: BFS
# as bfs will only search for depth k+1 until the depth k all be visited,
# thus use bfs could quickly calculate the last depth nodes' sum
###

from typing import Optional
import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        dq = collections.deque()
        dq.append([root, 1])
        cur_depth = 1
        _sum = 0

        while True:
            if len(dq) == 0:
                break
            node, depth = dq.popleft()
            if depth == cur_depth:
                _sum += node.val
            else:
                _sum = node.val
                cur_depth = depth
            if node.left:
                dq.append([node.left, depth + 1])
            if node.right:
                dq.append([node.right, depth + 1])
        return _sum
