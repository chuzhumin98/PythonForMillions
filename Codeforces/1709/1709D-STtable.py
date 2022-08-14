###
# Solution: ST Table, also TLE for python code, we recode it with C++ and AC
# we can find that if delta_x and delta_y of s and f cannot be divided by k, then the robot cannot reach the finish cell,
# if so, then we need to ensure the robot could across the max height (x_i) block to do the operations
# that is just to calculate max(x_i) where i in the range of interval [s, t].
# if (n - xs) % k > (max(x_i) - xs) % k, then the goal could complete.
# this is a typical RMQ (range minimum question), we can use ST table or Segment Tree to calculate it in O(1) complexity.
# also, the construction of ST table is O(m * log m)
#
###

def get_rmq(low, high, rmqs, log_ns, exp2s_list):
    logn = log_ns[high - low + 1]
    max_height = max(rmqs[low][logn], rmqs[high - exp2s_list[logn] + 1][logn])
    return max_height

n, m = input().split()
n, m = int(n), int(m)
As = input().split()
As = [int(_) for _ in As]

exp2s_list = [1]
log_ns = [0 for _ in range(m+1)]
for i in range(2, m+1):
    log_ns[i] = log_ns[i//2] + 1

R = log_ns[m] + 1
for i in range(1, R):
    exp2s_list.append(exp2s_list[-1] * 2)
rmqs = [[0 for _ in range(R)] for __ in range(m)]

for i in range(m):
    rmqs[i][0] = As[i]
for j in range(1, R):
    for i in range(m):
        rmqs[i][j] = rmqs[i][j-1]
        idx_new = i + exp2s_list[j-1]
        if idx_new < m:
            rmqs[i][j] = max(rmqs[i][j], rmqs[idx_new][j-1])

q = int(input())
for _ in range(q):
    arr = input().split()
    arr = [int(i) for i in arr]
    arr[1] -= 1
    arr[3] -= 1
    deltaX, deltaY = abs(arr[0] - arr[2]), abs(arr[1] - arr[3])
    K = arr[4]

    if deltaX % K == 0 and deltaY % K == 0:
        ylow, yhigh = min(arr[1], arr[3]), max(arr[1], arr[3])
        max_height = get_rmq(ylow, yhigh, rmqs, log_ns, exp2s_list)
        if max_height < arr[0]:
            print("YES")
        elif (n - arr[0]) // K <= (max_height - arr[0]) // K:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")
