###
# Solution: math
# goal: to find the min x >= N, satisfy that the 2-base representation of x contains
# no more than K "1" digit
# to gain answer faster, we can skip the try val with the step of lowbit(val),
# instead of step 1
###

def lowbit(n):
    return n & (-n)

def get_digits(n):
    _sum = 0
    while n > 0:
        n -= lowbit(n)
        _sum += 1
    return _sum

N, K = input().split()
N, K = int(N), int(K)
_sum = 0
while True:
    if get_digits(N) <= K:
        break
    delta = lowbit(N)
    _sum += delta
    N += delta
print(_sum)

