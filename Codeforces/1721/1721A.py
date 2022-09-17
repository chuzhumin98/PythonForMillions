t = int(input())
for _ in range(t):
    s = input().strip()
    s += input().strip()
    s = sorted([char for char in s])
    if s[0] == s[3]:
        print(0)
    elif s[0] == s[2] or s[1] == s[3]:
        print(1)
    elif s[0] == s[1] and s[2] == s[3]:
        print(1)
    elif s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        print(2)
    else:
        print(3)