###
# Solution: bfs
# first we use bfs to mark each grid belongs to which connection block, as well as record each connection block's size
# then for each grid == 0, we try to change it into island, also to calculate it's connected island area
# (that is just 1 + left-right-top-bottom grid unique connection blocks' sum)
# if grid == 0 does not exist, then directly return n^2
###
from typing import List
class Solution:
    def spread(self, x, y, grid, dq, cur_block):
        if grid[x][y] == 1:
            grid[x][y] = cur_block
            self.cnt_bsize += 1
            dq.append([x, y])


    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        blocks = [[grid[i][j] for j in range(n)] for i in range(n)]
        self.blocks_size = dict()
        maxv = 0
        cur_block = 2
        for i in range(n):
            for j in range(n):
                if blocks[i][j] == 1:
                    self.cnt_bsize = 1
                    self.neighbor_max = 0
                    blocks[i][j] = cur_block
                    dq = collections.deque()
                    dq.append([i, j])
                    while len(dq) > 0:
                        ii, jj = dq.popleft()
                        if ii > 0:
                            self.spread(ii-1, jj, blocks, dq, cur_block)
                        if jj > 0:
                            self.spread(ii, jj-1, blocks, dq, cur_block)
                        if ii < n-1:
                            self.spread(ii+1, jj, blocks, dq, cur_block)
                        if jj < n-1:
                            self.spread(ii, jj+1, blocks, dq, cur_block)
                    self.blocks_size[cur_block] = self.cnt_bsize
                    cur_block += 1
                    maxv = max(maxv, self.cnt_bsize)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    size = 1
                    used_set = set()
                    if i > 0:
                        val = blocks[i-1][j]
                        if val > 1 and val not in used_set:
                            used_set.add(val)
                            size += self.blocks_size[val]
                    if j > 0:
                        val = blocks[i][j-1]
                        if val > 1 and val not in used_set:
                            used_set.add(val)
                            size += self.blocks_size[val]
                    if i < n-1:
                        val = blocks[i+1][j]
                        if val > 1 and val not in used_set:
                            used_set.add(val)
                            size += self.blocks_size[val]
                    if j < n-1:
                        val = blocks[i][j+1]
                        if val > 1 and val not in used_set:
                            used_set.add(val)
                            size += self.blocks_size[val]
                    maxv = max(maxv, size)
        return maxv
