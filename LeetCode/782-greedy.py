###
# Solution: greedy
# we find that the row and column operation do not change the each row's relative relation, for example,
# if one row is 10010, another row is 00001, the different values num is 3, then after swap operation, the difference doesnot change
# thus, we conclude the chessable matrix with the following three constraints:
# (1) each row's difference num is n or 0, i.e. all the numbers of two rows are equivalent or reversed;
# (2) each row's 0 and 1 count delta is -1, 0, 1
# (3) each column's 0 and 1 count delta is -1, 0, 1
# then, we use greedy strategy, to set all even index position of first row and first column to be 0/1, we count++ for
# each we meet not to be 0/1, then the optimal choice (0/1) could be the min operation number
###

from typing import List
class Solution:
    def get_change(self, arr, s0):
        _sum = 0
        for i, num in enumerate(arr):
            if i % 2 == 0:
                if num != s0:
                    _sum += 1
        # print(f'get_change({arr}, {s0}) = {_sum}')
        return _sum

    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        for i in range(1, n):
            _sum = 0
            for j, num in enumerate(board[i]):
                _sum += abs(board[0][j] - num)
            if _sum != 0 and _sum != n:
                return -1
        delta1_0_c = 0
        for num in board[0]:
            delta1_0_c += 1 if num == 1 else -1
        if abs(delta1_0_c) > 1:
            return -1
        delta1_0_r = 0
        for i in range(n):
            delta1_0_r += 1 if board[i][0] == 1 else -1
        if abs(delta1_0_r) > 1:
            return -1

        _sum_col = 0
        _sum_row = 0
        row0 = [board[i][0] for i in range(n)]
        if n % 2 == 0:
            _sum_col = min(self.get_change(board[0], 0), self.get_change(board[0], 1))
            _sum_row = min(self.get_change(row0, 0), self.get_change(row0, 1))
        else:
            _sum_col = self.get_change(board[0], 1 if delta1_0_c == 1 else 0)
            _sum_row = self.get_change(row0, 1 if delta1_0_r == 1 else 0)
        # print(f'sum_col = {_sum_col}, sum_row = {_sum_row}')
        return _sum_col + _sum_row
