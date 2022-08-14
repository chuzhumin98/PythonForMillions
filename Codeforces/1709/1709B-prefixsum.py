###
# simple problem, no need to say; you need to precalculate a prefix sum and postfix sum to obtain O(1) for query
###

n, m = input().split()
n, m = int(n), int(m)

As = input().split()
As = [int(_) for _ in As]

prefix_sums = [0]
for i in range(n-1):
    value = 0 if As[i+1] >= As[i] else As[i] - As[i+1]
    prefix_sums.append(prefix_sums[-1] + value)

postfix_sums = [0]
for i in range(n-1, 0, -1):
    value = 0 if As[i-1] >= As[i] else As[i] - As[i-1]
    postfix_sums.append(postfix_sums[-1] + value)

for _ in range(m):
    s, t = input().split()
    s, t = int(s)-1, int(t)-1
    if s < t:
        print(prefix_sums[t] - prefix_sums[s])
    else:
        print(postfix_sums[n-1-t] - postfix_sums[n-1-s])
