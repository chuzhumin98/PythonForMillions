###
# Solution: Greedy
# consider from small rate to large rate child, then we greedy to give the child the least candy as possible, that is
# f(k) = max(1, f(k-1)+ 1 if r[k] > r[k-1], f(k+1)+1 if r[k] > r[k+1])
###
from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        ratings_items = [[rate, idx] for idx, rate in enumerate(ratings)]
        ratings_items.sort(key=lambda x: x[0])
        fs = [1 for _ in range(len(ratings))]
        for ri, idx in ratings_items:
            if idx > 0:
                if ri > ratings[idx-1]:
                    fs[idx] = max(fs[idx], fs[idx-1] + 1)
            if idx < len(ratings) - 1:
                if ri > ratings[idx + 1]:
                    fs[idx] = max(fs[idx], fs[idx+1] + 1)
        return sum(fs)