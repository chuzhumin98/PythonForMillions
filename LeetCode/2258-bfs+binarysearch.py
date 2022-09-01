###
# Solution: bfs + binary search
# we first use bfs to record the min fired time of each position
# then we find that when the start time become larger, the arriviable status would tend to be unarrivable,
# thus, we can use binary search to find the first unarrived status (set the high to be the lastest fired time + 1, to
# record for the infinity), to check if start time t is possible to arrive the safe position, we also use the bfs!!!
###

from typing import List
import collections
class Solution:
    def check(self, x, y, s, dq, arrived, unarr, m, n):
        if arrived[x][y] > s:
            if unarr[x][y] > s or (unarr[x][y] == s and x + y == m + n - 2):
                arrived[x][y] = s
                dq.append([x, y, s])
            else:
                arrived[x][y] = -s

    def binary_search_check(self, step0, unarr, m, n):
        if unarr[0][0] <= step0:
            return False
        arrived = [[self.INF for _ in range(n)] for __ in range(m)]
        dq = collections.deque()
        dq.append([0, 0, step0])
        arrived[0][0] = step0
        while len(dq) > 0:
            x, y, s = dq.popleft()
            s += 1
            if x < m - 1:
                self.check(x + 1, y, s, dq, arrived, unarr, m, n)
            if y < n - 1:
                self.check(x, y + 1, s, dq, arrived, unarr, m, n)
            if x > 0:
                self.check(x - 1, y, s, dq, arrived, unarr, m, n)
            if y > 0:
                self.check(x, y - 1, s, dq, arrived, unarr, m, n)
        if arrived[m - 1][n - 1] >= 0 and arrived[m - 1][n - 1] < self.INF:
            return True
        else:
            return False

    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        self.INF = 1 << 30
        first_unarrivable = [[self.INF for __ in range(n)] for _ in range(m)]
        dq = collections.deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    first_unarrivable[i][j] = 0
                    dq.append([i, j, 0])
                elif grid[i][j] == 2:
                    first_unarrivable[i][j] = 0
        # dfs for fire
        step = 0
        while len(dq) > 0:
            x, y, step = dq.popleft()
            step += 1
            if x < m - 1:
                if first_unarrivable[x + 1][y] > step:
                    first_unarrivable[x + 1][y] = step
                    dq.append([x + 1, y, step])
            if y < n - 1:
                if first_unarrivable[x][y + 1] > step:
                    first_unarrivable[x][y + 1] = step
                    dq.append([x, y + 1, step])
            if x > 0:
                if first_unarrivable[x - 1][y] > step:
                    first_unarrivable[x - 1][y] = step
                    dq.append([x - 1, y, step])
            if y > 0:
                if first_unarrivable[x][y - 1] > step:
                    first_unarrivable[x][y - 1] = step
                    dq.append([x, y - 1, step])

        low, high = 0, step
        while low < high:
            mid = (low + high) // 2
            if self.binary_search_check(mid, first_unarrivable, m, n):
                low = mid + 1
            else:
                high = mid - 1
        # print(first_unarrivable)
        # print(low, high)
        if self.binary_search_check(low, first_unarrivable, m, n):
            if low == step:
                return 1000000000
            return low
        else:
            return low - 1



