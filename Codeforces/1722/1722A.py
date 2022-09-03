###
# simple problem, no need to say
###
t = int(input())
template = ''.join(sorted('Timur'))
for _ in range(t):
    n = int(input())
    s = input().strip()
    s_sort = ''.join(sorted(s))
    if s_sort == template:
        print('YES')
    else:
        print("NO")