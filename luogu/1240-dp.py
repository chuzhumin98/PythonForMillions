###
# Solution: dp
# note that for n , each column grids num is 1, 3, ... 2n-3, 2n-1, 2n-3, ..., 3, 1
# we can transpose it into 1, 1, 3, 3, ...,  2n-3, 2n-3, 2n-1 (named N array)
# let f(x, y) be the methods number that left x columns can place y zhuhous, then
# f(x, y) = f(x-1, y) + f(x-1, y-1) * (N[y] - y + 1)
###

P = 504
n, k = input().split()
n, k = int(n), int(k)
if k >= 2 * n - 1:
    print(0)
elif k == 0:
    print(1)
else:
    fs = [[0 for __ in range(k+1)] for _ in range(2*n-1)]
    fs[0][0] = 1
    fs[0][1] = 1
    for i in range(1, 2 * n - 1):
        s = 1 + (i // 2) * 2
        fs[i][0] = fs[i-1][0]
        for j in range(1, min(s,k)+1):
            fs[i][j] = (fs[i-1][j] + fs[i-1][j-1] * (s - j + 1)) % P
    print(fs[2*n-2][k])