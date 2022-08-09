###
# Solution: dp
# suppose f(i, j) as the edit distance for word1[:i] and word2[:j], then
# if word1[i] == word2[j], then f(i+1, j+1) = min(f(i, j), f(i+1, j)+1, f(i, j+1)+1);
# else f(i+1, j+1) = min(f(i, j)+1, f(i+1, j)+1, f(i, j+1)+1);
# thus, we can get f(len(word1)-1, len(word2)-1) in O(m*n) time
###

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        min_dists = [[100000 for _ in range(n + 1)] for __ in range(m + 1)]

        for i in range(m + 1):
            min_dists[i][0] = i
        for j in range(n + 1):
            min_dists[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    min_dists[i][j] = min(min_dists[i - 1][j - 1], min_dists[i][j - 1] + 1, min_dists[i - 1][j] + 1)
                else:
                    min_dists[i][j] = min(min_dists[i - 1][j - 1] + 1, min_dists[i][j - 1] + 1, min_dists[i - 1][j] + 1)

        return min_dists[m][n]


if __name__ == '__main__':
    word1 = "intention"
    word2 = "execution"

    print(Solution().minDistance(word1, word2))