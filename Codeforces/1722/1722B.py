###
# simple problem, no need to say
###
t = int(input())
for _ in range(t):
    n = int(input())
    s1 = input().strip()
    s2 = input().strip()
    if s1.replace('G', 'B') == s2.replace('G', 'B'):
        print("YES")
    else:
        print("NO")