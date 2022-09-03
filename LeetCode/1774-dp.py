###
# Solution: dp
# a simple multi-bag dp problem, as we no need to maximize the bag size, only to consider the value,
# let f(n) be the bool value to store if value n can reach, then
# for the base cost c_bi, f(c_bi) = true;
# for each topping cost c_ti, f(n) = true if in the last iteration f(n) or f(n-c_ti) or f(n-c_ti*2) is true
###

from typing import List

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        TMAX = target + 1 + 10000
        can_reach = [False for _ in range(TMAX)]
        for cost in baseCosts:
            can_reach[cost] = True
        for cost in toppingCosts:
            for i in range(target, -1, -1): # if i > target, then i + c is further than i with respect to target
                if can_reach[i]:
                    can_reach[i + cost] = True
                    if i + cost * 2 < TMAX:
                        can_reach[i + cost * 2] = True
        min_delta, min_idx = 10000, 0
        for i in range(TMAX):
            if can_reach[i]:
                if abs(i - target) < min_delta:
                    min_delta = abs(i - target)
                    min_idx = i
        return min_idx