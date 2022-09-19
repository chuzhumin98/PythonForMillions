from typing import List
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight



class Solution:
    def buildNode(self, lr, rr, lc, rc, node):
        cnt = self.presums[rr][rc] + self.presums[lr][lc] - self.presums[lr][rc] - self.presums[rr][lc]
        if cnt == (rr - lr) * (rc - lc):
            node.val = 1
            node.isLeaf = 1
        elif cnt == 0:
            node.val = 0
            node.isLeaf = 1
        else:
            mr, mc = (lr + rr) // 2, (lc + rc) // 2
            node.topLeft = Node(0, 0, None, None, None, None)
            node.topRight = Node(0, 0, None, None, None, None)
            node.bottomLeft = Node(0, 0, None, None, None, None)
            node.bottomRight = Node(0, 0, None, None, None, None)
            self.buildNode(lr, mr, lc, mc, node.topLeft)
            self.buildNode(lr, mr, mc, rc, node.topRight)
            self.buildNode(mr, rr, lc, mc, node.bottomLeft)
            self.buildNode(mr, rr, mc, rc, node.bottomRight)

    def construct(self, grid: List[List[int]]) -> 'Node':
        self.n = len(grid)
        self.presums = [[0 for _ in range(self.n + 1)] for __ in range(self.n + 1)]
        for i in range(1, self.n + 1):
            for j in range(1, self.n + 1):
                self.presums[i][j] = self.presums[i - 1][j] + self.presums[i][j - 1] + grid[i - 1][j - 1] - \
                                     self.presums[i - 1][j - 1]
        root = Node(1, 0, None, None, None, None)
        self.buildNode(0, self.n, 0, self.n, root)
        return root
