###
# Solution: differential array
# denote L(k) = \sum_{i<=k} countUniqueChars(s[i:k]) (contain i and k)
# we find that L(k) - L(k-1) = (k - lastappearidx(s[k])) - (lastappearidx(s[k]) - secondlastappearidx(s[k]))
###

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        lnum = 26
        last_idxs = [-1 for _ in range(lnum)]
        llast_idxs = [-1 for _ in range(lnum)]
        _sum_this = 0
        _sum_total = 0
        for i, char in enumerate(s):
            cidx = ord(char) - ord('A')
            _sum_this += (i - last_idxs[cidx]) - (last_idxs[cidx] - llast_idxs[cidx])
            _sum_total += _sum_this

            llast_idxs[cidx] = last_idxs[cidx]
            last_idxs[cidx] = i
        return _sum_total