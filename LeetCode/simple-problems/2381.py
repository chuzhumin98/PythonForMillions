from typing import List
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        deltas = [0 for _ in range(len(s) + 1)]
        for si, ei, di in shifts:
            if di == 0:
                deltas[si] -= 1
                deltas[ei + 1] += 1
            else:
                deltas[si] += 1
                deltas[ei + 1] -= 1
        _sum = 0
        s_new = ''
        for i in range(len(s)):
            _sum += deltas[i]
            char_id = (ord(s[i]) + _sum - ord('a')) % 26 + ord('a')
            s_new += chr(char_id)
        return s_new