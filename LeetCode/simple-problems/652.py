from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, node):
        str_left, str_right = '', ''
        if node.left:
            str_left = self.dfs(node.left)
        if node.right:
            str_right = self.dfs(node.right)
        str_total = f'{node.val}({str_left})({str_right})'
        if str_total not in self.str_cnts:
            self.str_cnts[str_total] = [node, 1]
        else:
            self.str_cnts[str_total][1] += 1
        return str_total

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.str_cnts = dict()
        self.dfs(root)
        res = []
        for key in self.str_cnts:
            if self.str_cnts[key][1] > 1:
                res.append(self.str_cnts[key][0])
        return res