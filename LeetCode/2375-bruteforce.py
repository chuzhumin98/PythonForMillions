###
# Solution: bruteforce, no need to say more
###

class Solution:
    def next_permutation(self, arr):
        tail_arr = [arr[-1]]
        idx = len(arr) - 2
        while True:
            if idx < 0:
                break
            if arr[idx] < tail_arr[-1]:
                break
            tail_arr.append(arr[idx])
            idx -= 1
        if idx < 0:
            return None
        arr_new = [num for num in arr[:idx]]
        first2le_idx = 0
        while True:
            if tail_arr[first2le_idx] > arr[idx]:
                break
            first2le_idx += 1
        arr_new.append(tail_arr[first2le_idx])
        tail_arr[first2le_idx] = arr[idx]
        for num in tail_arr:
            arr_new.append(num)
        return arr_new

    def is_valid(self, pattern, perm):
        for i, pat in enumerate(pattern):
            if pat == 'I':
                if perm[i + 1] < perm[i]:
                    return False
            else:
                if perm[i + 1] > perm[i]:
                    return False
        return True

    def smallestNumber(self, pattern: str) -> str:
        perm = list(range(1, len(pattern) + 2))
        while True:
            if self.is_valid(pattern, perm):
                break
            perm = self.next_permutation(perm)
            if not perm:
                break
        return ''.join([str(_) for _ in perm])

if __name__ == '__main__':
    pattern = "IIIDIDDD"
    print(Solution().smallestNumber(pattern))