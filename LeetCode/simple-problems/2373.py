from typing import List
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        output = [[0 for __ in range(n - 2)] for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                output[i][j] = max([max([grid[ii][jj] for ii in range(i, i + 3)]) for jj in range(j, j + 3)])
        return output
