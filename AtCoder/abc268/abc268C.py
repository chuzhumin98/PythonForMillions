N = int(input())
ps = input().split()
ps = [int(i) for i in ps]

cnts = [0 for _ in range(N)]

for i, p in enumerate(ps):
    val = ((i-1) - p) % N
    cnts[val] += 1
    cnts[(val+1) % N] += 1
    cnts[(val + 2) % N] += 1

print(max(cnts))