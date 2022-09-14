from typing import List
class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        if 4 * boardingCost <= runningCost:
            return -1
        maxv, maxidx = -(1 << 31), -1
        _rm_user = 0
        profit, cnt = 0, 0
        for c in customers:
            cnt += 1
            _rm_user += c
            val = min(_rm_user, 4)
            _rm_user -= val
            profit += val * boardingCost - runningCost
            if profit > maxv:
                maxv = profit
                maxidx = cnt
        while _rm_user > 0:
            val = min(_rm_user, 4)
            cnt += 1
            profit += val * boardingCost - runningCost
            if profit > maxv:
                maxv = profit
                maxidx = cnt
            _rm_user -= val
        if maxv <= 0:
            return -1
        else:
            return maxidx