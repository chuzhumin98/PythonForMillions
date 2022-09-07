from typing import List
class Solution:
    def dfs(self, n):
        if n == self.n:
            self.ans.append(''.join(self.path))
            return
        for char in self.nums[self.idxs[n]]:
            self.path.append(char)
            self.dfs(n+1)
            self.path.pop()


    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        self.nums = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        self.idxs = [ord(d) - ord('2') for d in digits]
        self.n = len(self.idxs)
        self.ans = []
        self.path = []
        self.dfs(0)
        return self.ans