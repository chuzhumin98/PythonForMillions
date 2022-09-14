from typing import List
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        m = n // 20
        return sum(arr[m:n-m]) / float(n - 2 * m)