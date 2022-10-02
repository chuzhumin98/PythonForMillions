###
# Solution: greedy
# for each time, we get the sum of the total cycle S, if T >= S, then we directly cycled T / S rounds; T -> T % S
# then we visit each remained numbers in order, remove the unaffordable items, then start next iteration until
# the remained number set is empty
###

n, T = input().split()
n, T = int(n), int(T)
arr = input().split()
arr = [int(i) for i in arr]
_sum = sum(arr)

_cnt = T // _sum
T -= _cnt * _sum
_cnt *= n

while len(arr) > 0:
    arr_new = []
    _sum = 0
    for num in arr:
        if num <= T:
            T -= num
            _cnt += 1
            arr_new.append(num)
            _sum += num
    arr = arr_new
    if _sum > 0:
        _cnt += len(arr) * (T // _sum)
        T %= _sum

print(_cnt)
