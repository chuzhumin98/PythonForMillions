###
# Solution: dp
# as the alphabet set is only length 26, also, for the same letter, when the last located index become larger, the longest string
# is no smaller than the smaller located index one.
# thus, we only need to record the last located index for each letter (array ll),
# f(n) represents when the string ends located at index n, then
# f(n) = max(1, f(ll[char]) + 1) , where char is in the region s[n] - k to s[n] + k
# the total complexity is O(2k * n)
###

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        alphbet = 'abcdefghijklmnopqrstuvwxyz'
        alphbet_idx = dict()
        for idx, char in enumerate(alphbet):
            alphbet_idx[char] = idx
        inf_value = 1 << 30
        last_letter_idx = [inf_value for _ in range(26)]

        max_len_subs = [1 for _ in range(len(s))]
        last_letter_idx[alphbet_idx[s[0]]] = 0
        for idx in range(1, len(s)):
            cidx = alphbet_idx[s[idx]]
            for i in range(max(0, cidx - k), min(26, cidx + k + 1)):
                if last_letter_idx[i] != inf_value:
                    max_len_subs[idx] = max(max_len_subs[idx], max_len_subs[last_letter_idx[i]] + 1)
            last_letter_idx[cidx] = idx
        return max(max_len_subs)

if __name__ == '__main__':
    s = "acfgbd"
    k = 2
    print(Solution().longestIdealString(s, k))