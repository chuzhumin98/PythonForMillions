###
# Solution: dp
# let f(m, b) be the subsequences number of a[:m] ends with char b, then
# if a[m] = '1', f(m+1, 0) = f(m, 0), f(m+1, 1) = f(m, 0) + f(m, 1) + 1;
# if a[m] = '0', f(m+1, 0) = f(m, 0) + f(m, 1), f(m+1, 1) = f(m, 1)
# then total subsequences number is f(N-1, 0) + f(N-1, 1) + I('0' in a)
###
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        P = (10 ** 9) + 7
        fs = [[0, 0] for _ in range(len(binary))]
        if binary[0] == '1':
            fs[0][1] = 1
        for i in range(1, len(binary)):
            if binary[i] == '1':
                fs[i][0] = fs[i-1][0]
                fs[i][1] = (fs[i-1][0] + fs[i-1][1] + 1) % P
            else:
                fs[i][0] = (fs[i-1][0] + fs[i-1][1]) % P
                fs[i][1] = fs[i-1][1]
        if binary.find('0') > -1:
            return (fs[-1][0] + fs[-1][1] + 1) % P
        else:
            return (fs[-1][0] + fs[-1][1]) % P