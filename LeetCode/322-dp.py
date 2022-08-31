###
# Solution: dp
# multi-bags dp, let f(n) be the min coins to collect n value coin, then
# f(n) = min_{c \in coins} { f(n-c) } + 1
###

from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = 1 << 20
        fs = [INF for i in range(amount+1)]
        fs[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if coin <= i:
                    fs[i] = min(fs[i], fs[i - coin] + 1)
        if fs[amount] < INF:
            return fs[amount]
        else:
            return -1