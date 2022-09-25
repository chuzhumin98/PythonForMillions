###
# Solution: tree dp
# tree dp, let f(node, dnode, dtree) be the min operation num to make the subtree with root = node all close (with dnode = 1
# if node change status once, 0 with no change; dtree = 1 with node-subtree change status once, 0 with no change)
# then node's status s = (node.val + dnode + dtree) % 2,
# if s = 0, we can do nothing on it or push button 2 and 3 (others (1+2, 1+3) are
# useless, that is f(node, dnode, dtree) = min(f(node.left, 0, dtree) + f(node.right, 0, dtree), 2 + f(node.left, 1, 1-dtree) + f(node.right, 1, 1-dtree)
# if s = 1, we can push button 1 or 2 or 3 or 1+2+3, that is
# f(node, dnode, dtree) = min( 1+f(node.left, 0, dtree)+f(node.right, 0, dtree), 1+f(node.left, 1, dtree)+f(node.right,1,dtree),
#                              1+f(node.left, 0, 1-dtree)+f(node.right, 0, 1-dtree), 3+f(node.left, 1, 1-dtree)+f(node.right, 1, 1-dtree) )
###
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def get_min(self, node, dnode, dtree):
        if not node:
            return 0
        if type(node.val) != int:
            idx = 1 + dnode * 2 + dtree
            if node.val[idx] != None:
                return node.val[idx]
        else:
            node.val = [node.val, None, None, None, None]
        val = (node.val[0] + dnode + dtree) % 2
        if val == 0:
            minv = min(self.get_min(node.left, 0, dtree) + self.get_min(node.right, 0, dtree),
                       2 + self.get_min(node.left, 1, 1-dtree) + self.get_min(node.right, 1, 1-dtree))
        else:
            minv = min(1 + self.get_min(node.left, 0, dtree) + self.get_min(node.right, 0, dtree),
                       1 + self.get_min(node.left, 1, dtree) + self.get_min(node.right, 1, dtree),
                       1 + self.get_min(node.left, 0, 1 - dtree) + self.get_min(node.right, 0, 1 - dtree),
                       3 + self.get_min(node.left, 1, 1-dtree) + self.get_min(node.right, 1, 1-dtree))

        idx = 1 + dnode * 2 + dtree
        node.val[idx] = minv
        return minv




    def closeLampInTree(self, root: TreeNode) -> int:
        return self.get_min(root, 0, 0)



