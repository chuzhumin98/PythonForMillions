###
# Solution: math
# to make A step min as possible, we need to only use A in the important moment, that is:
# to swap odd and even wrong, as B step only can rerange the odd indexes and even indexes
# then we can split the steps with three parts:
# (1) put the wrong odd/even value into the leftmost indexes;
# (2) swap the wrong odd/even value pairwise with A step;
# (3) rearrange the even values and odd values seperately
###
N = int(input())
arr = input().split()
arr = [int(i) for i in arr]

strs = ''
oper_total = 0

cnt = 0
for i in range((N+1)//2):
    if arr[i*2] % 2 == 0:
        for j in range(i-1, -1, -1):
            idx = j * 2
            strs += f'B {idx+1}\n'
            oper_total += 1
            arr[idx], arr[idx + 2] = arr[idx + 2], arr[idx]
        cnt += 1

for i in range(N//2):
    if arr[i*2+1] % 2 == 1:
        for j in range(i-1, -1, -1):
            idx = j * 2 + 1
            strs += f'B {idx+1}\n'
            oper_total += 1
            arr[idx], arr[idx + 2] = arr[idx + 2], arr[idx]

for i in range(cnt):
    idx = i * 2
    strs += f'A {idx+1}\n'
    oper_total += 1
    arr[idx], arr[idx+1] = arr[idx+1], arr[idx]

for i in range((N-1)//2):
    for j in range(((N-1)//2) - i):
        idx = j * 2
        if arr[idx] > arr[idx+2]:
            strs += f'B {idx+1}\n'
            oper_total += 1
            arr[idx], arr[idx + 2] = arr[idx + 2], arr[idx]

for i in range((N // 2) - 1):
    for j in range((N//2) - 1 - i):
        idx = j * 2 + 1
        if arr[idx] > arr[idx+2]:
            strs += f'B {idx+1}\n'
            oper_total += 1
            arr[idx], arr[idx + 2] = arr[idx + 2], arr[idx]


print(oper_total)
print(strs, end='')