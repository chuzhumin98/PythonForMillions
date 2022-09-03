###
# simple problem, no need to say
###
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    _sum = 0
    deltas = []
    for i in range(n):
        if s[i] == 'L':
            _sum += i
            deltas.append(max(0, n-1-2*i))
        else:
            _sum += n - 1 - i
            deltas.append(max(0, 2*i+1-n))
    deltas.sort(reverse=True)
    _ans = [_sum]
    for delta in deltas:
        _ans.append(_ans[-1] + delta)
    print(' '.join([str(i) for i in _ans[1:]]))