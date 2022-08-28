###
# Solution: graph + Dijkstra Algorithm
# this is a typical "Y"-structure min path, we just to find a pivot Y, then min_path = Dist(src1, Y) + Dist(src2, Y) + Dist(Y, end)
# Y could be any point (include src1, src2, end), for the Dist(src1, Y), Dist(src2, Y), we can use Dijkstra algorithm to calculate the min path;
# for the Dist(Y, end), we reversed the edges, and then can use Dijkstra algorithm to calculate
###

import heapq
from typing import List
class Solution:
    def dijkstra(self, links, s):
        used = set()
        minV = [self.INF for _ in range(self.n)]
        min_candidates = [[0, s]]
        heapq.heapify(min_candidates)
        while len(used) < self.n and len(min_candidates) > 0:
            mdist, node = heapq.heappop(min_candidates)
            while node in used and len(min_candidates) > 0:
                mdist, node = heapq.heappop(min_candidates)
            if node in used:
                break
            minV[node] = mdist
            used.add(node)
            for t, w in links[node]:
                heapq.heappush(min_candidates, [mdist + w, t])
        return minV

    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        self.n = n
        self.INF = 1e12
        links = [[] for _ in range(n)]
        links_rv = [[] for _ in range(n)]
        for f, t, w in edges:
            links[f].append([t, w])
            links_rv[t].append([f, w])
        src12p = self.dijkstra(links, src1)
        src22p = self.dijkstra(links, src2)
        p2dest = self.dijkstra(links_rv, dest)
        # print(src12p, src22p, p2dest)
        min_total = src12p[0] + src22p[0] + p2dest[0]
        for i in range(1, n):
            min_total = min(min_total, src12p[i] + src22p[i] + p2dest[i])
        return min_total if min_total < self.INF else -1
