###
# Solution: dp
# range dp, let f(c, m, n) be the number of huiwen substring started with char c and taken from interval [m, n]
# then f(c, m, m) = I(s[m] = c), f(c, m, n) = 0 if m > n
# f(c, m, n) = (1) if s[m] = s[n] = c, 2 + sum(ci) f(ci, m+1, n-1);
#              (2) if s[m] = c != s[n], f(c, m, n-1);
#              (3) if s[m] != c = s[n], f(c, m+1, n);
#              (4) if s[m] != c != s[n], f(c, m+1, n-1);
###
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        P = (10 ** 9) + 7
        ls = 'abcd'
        l2idxs = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
        n = len(s)
        fs = [[[0 for ___ in range(n)] for __ in range(n)] for _ in range(4)]
        for i in range(n):
            fs[l2idxs[s[i]]][i][i] = 1
        for j in range(1, n):
            for i in range(n - j):
                cl, ch = l2idxs[s[i]], l2idxs[s[i + j]]
                for k in range(4):
                    if cl == k and ch == k:
                        fs[k][i][i + j] = (2 + fs[0][i + 1][i + j - 1] + fs[1][i + 1][i + j - 1] + fs[2][i + 1][
                            i + j - 1] + fs[3][i + 1][i + j - 1]) % P
                    elif cl == k:
                        fs[k][i][i + j] = fs[k][i][i + j - 1]
                    elif ch == k:
                        fs[k][i][i + j] = fs[k][i + 1][i + j]
                    else:
                        fs[k][i][i + j] = fs[k][i + 1][i + j - 1]
        _sum = 0
        for i in range(4):
            _sum = (_sum + fs[i][0][n - 1]) % P
        return _sum
