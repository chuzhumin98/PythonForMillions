###
# Solution: dp
# f(x, t) represents the number of ways that clip reaches position x in time t
# the recursive formula could be: f(x, t) = \sum_{x-kt*i >= 0} f(x-kt*i, t-1), where kt = t + k - 1
# note that the minimum reachable position x_min(t) = \sum_{i=1}^t (k + i - 1), so that t_max = O(n^0.5)
# also, we can find that f(x, t) = \sum_{x-kt*i >= 0} f(x-kt*i, t-1) = f(x-kt, t-1) + \sum_{(x-kt)-kt*i >= 0} f(x-kt*i, t-1)
# = f(x-kt, t) + f(x-kt, t-1), so we can get each f(x,t) in O(1) complexity
# to reduce space complexity, we only need to record f(xi, t) and f(xi, t-1) in each time, that is O(n);
# time complexity is O(n^1.5).
# However, even this complexity, the code is TLE for data point 5, though I optimize the details, so we take the same
# idea to implement a C++ version code (to check in 1716D.cpp)
###

P = 998244353
n, k = input().strip().split()
n, k = int(n), int(k)

fs = [0 for _ in range(n+1)] # total fangans

fs_last = [0 for _ in range(n+1)]
fs_current = [0 for _ in range(n+1)]
fs_last[0] = 1

cnt = k
_min_value = 0
while True:
    for i in range(_min_value+cnt, n+1):
        fs_current[i] = fs_last[i - cnt] + fs_current[i - cnt]
        fs[i] = (fs[i] + fs_current[i]) % P

    _min_value += cnt
    cnt += 1
    if _min_value + cnt > n:
        break

    # fs_last = fs_current
    # fs_current = [0 for _ in range(n+1)]

    fs_last, fs_current = fs_current, fs_last
    for i in range(_min_value, _min_value+cnt):
        fs_current[i] = 0



print(' '.join([str(_) for _ in fs[1:]]))

