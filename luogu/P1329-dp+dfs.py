###
# Solution: dp with prune
# we define d_i = a_i - a_{i-1}, then d_i \in {-1, 1} for each i, a_i = d_1 + d_2 + ... + d_i
# also, we can get that the total sum s = a_0 + a_2 + ... + a_{n-1} = \sum_{i \in {1,2,...n-1}} (n-i) * d_i
# thus, s_norm = (s + n(n-1) / 2) / 2 = \sum_A, where A is any subset of {1, 2, ..., n-1}
# with brute force, the complexity is O(2^n), impossible!
# so we use dp with prune, we select numbers from n-1 to 1, suppose the total methods num f(k, total) = f(k+1, total) + f(k+1, total - k)
# where k is now concerned select number, total is the current select sum from n-1 to k
# if total > s_norm or total < s_norm - (1+2+...+(k-1), then we ignore this total (as the goal s_norm cannot be achieved!)
# then, the result num = f(1, s_norm), we can use f(1, s_norm) to inverse all possible path with DFS method!
# that is: for f(k, total), is f(k+1, total) > 0 then non-select k is a possible path; if f(k+1, total-k) > 0 then select k is a possible path
# we only need to select no more than 100 paths, so this part of complexity is no more than O(100*n)
###

def dfs(fs, idx, sum_of_pred, current_path, fangans_list, n):
    # print(f'dfs({idx}, {sum_of_pred}, {current_path})')
    if len(fangans_list) >= 100:
        return
    if idx == 0:
        current_path.append(1 if sum_of_pred > 0 else -1)
        fangans_list.append(list(reversed(current_path)))
        current_path.pop()
        return
    delta = n - idx - 1
    if sum_of_pred in fs[idx-1]:
        current_path.append(-1)
        dfs(fs, idx-1, sum_of_pred, current_path, fangans_list, n)
        current_path.pop()
    if sum_of_pred - delta in fs[idx-1]:
        current_path.append(1)
        dfs(fs, idx-1, sum_of_pred - delta, current_path, fangans_list, n)
        current_path.pop()



n, s = input().split()
n, s = int(n), int(s)

P = 1 << 64

if n == 1:
    if s == 0:
        print("1\n0")
    else:
        print(0)
else:
    one_sums = s + n * (n - 1) / 2
    if one_sums % 2 == 1:
        print(0)
    else:
        one_sums //= 2 # we need to calculate 1, 2, 3, ..., n-1 to one_sums
        sums_of_k = [0, 1]
        for i in range(2, n):
            sums_of_k.append(sums_of_k[-1] + i)

        if one_sums < 0 or one_sums > sums_of_k[-1]:
            print(0)
        else:
            fs = [{n-1: 1, 0: 1}] # from n-1 to 1
            for num in range(n-2, 0, -1):
                fs_pred = fs[-1]
                fs_new = dict()
                for pred_sum in fs_pred:
                    if pred_sum <= one_sums and pred_sum + sums_of_k[num-1] >= one_sums:
                        fs_new[pred_sum] = (fs_new.get(pred_sum, 0) + fs_pred[pred_sum]) % P
                    if pred_sum + num <= one_sums and pred_sum + sums_of_k[num] >= one_sums:
                        fs_new[pred_sum + num] = (fs_new.get(pred_sum + num, 0) + fs_pred[pred_sum]) % P
                fs.append(fs_new)

            if one_sums not in fs[-1]:
                print(0)
            else:
                print(fs[-1][one_sums])

                fangans_list = []
                dfs(fs, n-2, one_sums, [], fangans_list, n)

                for item in fangans_list:
                    fangan = [0]
                    for num in item:
                        fangan.append(fangan[-1] + num)
                    print(' '.join([str(_) for _ in fangan]))

                print([len(item) for item in fs])

