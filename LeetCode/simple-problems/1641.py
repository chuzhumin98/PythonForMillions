class Solution:
    def countVowelStrings(self, n: int) -> int:
        fs = [[1 for __ in range(5)] for _ in range(n)]
        for i in range(1, n):
            fs[i][0] = fs[i-1][0]
            for j in range(1, 5):
                fs[i][j] = fs[i-1][j] + fs[i][j-1]
        return sum(fs[-1])