###
# Solution: as the remove action only happens as the prefix of the array, we can just calculate starting from the end of the array. Then, when we met the first repeat value, directly return the length of the postfix
###

t = int(input())
for _ in range(t):
    n = int(input())
    As = input().split()
    As = [int(a) for a in As]
    aset = set()
    for a in As[::-1]:
        if a not in aset:
            aset.add(a)
        else:
            break
    print(n - len(aset))