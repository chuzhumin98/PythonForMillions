from typing import List
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        arr = [[] for _ in range(4)]
        for i in range(4):
            if i == 0:
                for j in range(len(arr1)):
                    arr[i].append(arr1[j] + arr2[j] + j)
            elif i == 1:
                for j in range(len(arr1)):
                    arr[i].append(arr1[j] - arr2[j] + j)
            elif i == 2:
                for j in range(len(arr1)):
                    arr[i].append(-arr1[j] + arr2[j] + j)
            else:
                for j in range(len(arr1)):
                    arr[i].append(-arr1[j] - arr2[j] + j)
        _maxv = 0
        for i in range(4):
            _maxv = max(_maxv, max(arr[i]) - min(arr[i]))
        return _maxv