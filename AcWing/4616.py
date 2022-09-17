import heapq
n, a, b, k = input().split()
n, a, b, k = int(n), int(a), int(b), int(k)
s = input().strip()

cnt_jian = 0
arr = []
_sum, sidx = 0, 0
for i, char in enumerate(s):
    if char == '1':
        if _sum > 0:
            arr.append([-_sum, sidx, i-1])
            cnt_jian += _sum // b
            _sum = 0
        sidx = i + 1

    else:
        _sum += 1

if _sum > 0:
    arr.append([-_sum, sidx, len(s)-1])
    cnt_jian += _sum // b

_cnt = 0
fs = []
heapq.heapify(arr)
while cnt_jian >= a:
    _sum, sidx, eidx = heapq.heappop(arr)
    split_idx = sidx + b
    cnt_jian -= 1
    heapq.heappush(arr, [_sum+b, split_idx, eidx])
    fs.append(split_idx-1)
    _cnt += 1
print(_cnt)
print(' '.join([str(i) for i in fs]))

