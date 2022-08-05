###
# Solution:
# We can use the DP algorithm to solve this problem
# let f(i), path(i), last(i), start(i) represents the minimum number of steps it will take to turn all the letters before (include itself) to be red (default value -1 represents no answer),
# the rightmost substring to select to take (i - k, i] to be red, the end position of the second rightmost substring to be selected, the position i - k
# the recursion formula would be f(i) = min_{0 < j <= km}(f(j)) + 1, where km is the longest matched postfix substring ended at position i, let j = jm that take the min value,
# then path(i) = the longest matched substring index, last(i) = jm, start(i) = i - length(longest matched substring)
# finally, f(s_len - 1) is the minimum step (-1 represents no answer), we can use path(i), last(i) and start(i) to recursively obtain the least step strategy
###

q = int(input())
for _ in range(q):
    s = str(input()).strip()
    n = int(input())
    subs = []
    for __ in range(n):
        subs.append(str(input()).strip())


    N = len(s)
    s_min_nums = [-1 for __ in range(N)]
    s_min_paths = [-1 for __ in range(N)]
    s_min_lastidxs = [-1 for __ in range(N)]
    s_min_substartidx = [-1 for __ in range(N)]
    for i in range(N):
        is_minus_one = False
        longest_match = 0
        longest_match_sub_idx = -1
        for j, sub in enumerate(subs):
            idx = i - len(sub)
            if idx == -1:
                if sub == s[:i+1]:
                    s_min_nums[i] = 1
                    s_min_paths[i] = j
                    s_min_lastidxs[i] = -1
                    s_min_substartidx[i] = 0
                    is_minus_one = True
                    break
            elif idx >= 0:
                if s[idx+1:i+1] == sub:
                    if longest_match < len(sub):
                        longest_match = len(sub)
                        longest_match_sub_idx = j
        if not is_minus_one and longest_match > 0:
            min_num_this = -1
            min_lastidx_this= -1
            for idx in range(i-longest_match, i):
                if s_min_nums[idx] != -1 and (s_min_nums[idx] + 1 < min_num_this or min_num_this == -1):
                    min_num_this = s_min_nums[idx] + 1
                    min_lastidx_this = idx
            s_min_nums[i] = min_num_this
            s_min_paths[i] = longest_match_sub_idx
            s_min_lastidxs[i] = min_lastidx_this
            s_min_substartidx[i] = i - longest_match + 1


    print(s_min_nums[-1])
    if s_min_nums[-1] >= 0:
        idx = N - 1
        while True:
            sub_idx = s_min_paths[idx]
            print(sub_idx+1, s_min_substartidx[idx]+1)
            idx = s_min_lastidxs[idx]
            if idx < 0:
                break