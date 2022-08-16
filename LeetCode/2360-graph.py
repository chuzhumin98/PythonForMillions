###
# Solution: graph visit
# we only need to record for every node start path; also record the visited node to prevent revisit
# if the visit comes to a cycle, then record its length, else remove it.
###

from typing import List

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        remain_edges = set(list(range(len(edges))))
        max_cycle = -1

        for ss in range(len(edges)):
            if len(remain_edges) == 0:
                break

            if ss not in remain_edges:
                continue

            remain_edges.remove(ss)
            points = {ss: 0}
            s = ss

            while True:
                s = edges[s]
                if s in points:
                    max_cycle = max(max_cycle, len(points) - points[s])
                    break
                if s == -1 or s not in remain_edges:
                    break

                points[s] = len(points)
                remain_edges.remove(s)
        return max_cycle

if __name__ == '__main__':
    edges = [3, 3, 4, 2, 3]
    print(Solution().longestCycle(edges))
