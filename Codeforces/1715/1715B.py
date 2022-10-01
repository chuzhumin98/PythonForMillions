t = int(input())
for _ in range(t):
    n, k, b, s = input().split()
    n, k, b, s = int(n), int(k), int(b), int(s)

    low_s, high_s = b * k, b * k + n * (k-1)
    if s >= low_s and s <= high_s:
        mode_total = s - low_s
        mode_all = mode_total // n
        left_mode = mode_total % n
        nums = [mode_all for __ in range(n)]
        nums[0] += low_s
        for i in range(left_mode):
            nums[i] += 1

        print(' '.join([str(i) for i in nums]))
    else:
        print(-1)