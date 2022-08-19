from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        _sum = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime and endTime[i] >= queryTime:
                _sum += 1
        return _sum