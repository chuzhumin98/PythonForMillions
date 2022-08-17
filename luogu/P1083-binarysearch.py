###
# Solution: binary search + difference array, TLE for python code
# to quickly hold for the interval modify (each minus d classrooms for day x to y
# we can use difference array, that is d[i] = a[i] - a[i-1]
# then a[i] = \sum_{j=0toi} d[i]
# so for the first k modifys, we can take O(n + k) to calculate for the a[i]
# then, we find that the remaining classroom is monotonically decreasing.
# so we can use binary search to find the first unsatisfy order,
# Complexity is O((m+n)*log m)
###

def check(arr, data, k): # check [0, k] is possible?
    deltas = [0 for _ in range(len(arr)+1)] # d[i] = arr'[i] - arr'[i-1]
    for d, x, y in data[:k+1]:
        deltas[x] += d
        deltas[y+1] -= d

    _sum = 0
    for i, num in enumerate(arr):
        _sum += deltas[i]
        if _sum > num:
            return False
    return True

def binary_search(arr, data, low, high):
    if low >= high:
        if check(arr, data, low):
            return low + 1
        else:
            return low
    mid = (low + high) >> 1
    if check(arr, data, mid):
        return binary_search(arr, data, mid+1, high)
    else:
        return binary_search(arr, data, low, mid-1)



n, m = input().split()
n, m = int(n), int(m)
arr = input().split()
arr = [int(i) for i in arr]

orders = []
for _ in range(m):
    data = input().split()
    data = [int(__) for __ in data]
    data[1] -= 1
    data[2] -= 1
    orders.append(data)

order_select = binary_search(arr, orders, 0, m-1)
if order_select == m:
    print(0)
else:
    print(f'-1\n{order_select + 1}')

