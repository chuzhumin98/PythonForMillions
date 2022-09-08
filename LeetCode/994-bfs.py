###
# Solution: bfs
# a bfs template problem, no need to say more
###
from typing import List
import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        _good = 0
        t_now = 0

        dq = collections.deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    _good += 1
                elif grid[i][j] == 2:
                    dq.append([i, j, 0])

        while _good > 0 and len(dq) > 0:
            x, y, t = dq.popleft()
            t += 1
            t_now = t
            if x > 0:
                if grid[x - 1][y] == 1:
                    grid[x - 1][y] = 2
                    _good -= 1
                    dq.append([x - 1, y, t])
            if y > 0:
                if grid[x][y - 1] == 1:
                    grid[x][y - 1] = 2
                    _good -= 1
                    dq.append([x, y - 1, t])
            if x < m - 1:
                if grid[x + 1][y] == 1:
                    grid[x + 1][y] = 2
                    _good -= 1
                    dq.append([x + 1, y, t])
            if y < n - 1:
                if grid[x][y + 1] == 1:
                    grid[x][y + 1] = 2
                    _good -= 1
                    dq.append([x, y + 1, t])

        if _good == 0:
            return t_now
        else:
            return -1

