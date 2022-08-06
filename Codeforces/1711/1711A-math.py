###
# Solution:
# As number 1 could divide any positive integer, so the potential min weight is 1.
# then we can construct the following permutation for n, with the property: gcd(n, n-1) = 1
# [n, 1, 2, ..., n-1]
###

t = int(input())
for _ in range(t):
    num = int(input())
    if num == 1:
        print(1)
    else:
        print(num, end=' ')
        print(' '.join([str(i) for i in range(1, num)]))
