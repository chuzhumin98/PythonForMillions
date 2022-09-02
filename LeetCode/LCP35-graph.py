###
# Solution: graph + Dijkstra algorithm
# in our graph, each vertex is (city, remain battery) status pair, totally (cnt + 1) * n,
# edge contains two types: (1). charge edge (c1, rb) -> (c1, rb + 1), edge weight is charge[c1];
# (2). tour edge (c1+d+i, c2+i), where (c1, c2) has a road length d
# we use Dijkstra algorithm to find the minimum path from (start, 0) to (end, 0), note that in this graph,
# total edge number is O(|e| + K*|e|) = O(K*|e|), where K = cnt + 1,
# thus, total complexity is O(K*|e|*log(K*|e|))
###

from typing import List
import heapq

class Solution:
    def electricCarPlan(self, paths: List[List[int]], cnt: int, start: int, end: int, charge: List[int]) -> int:
        INF = 1 << 30
        n = len(charge)
        edges = [[] for _ in range(n)]
        for a, b, d in paths:
            edges[a].append([b, d])
            edges[b].append([a, d])
        # status transfer: (node, k) -> (node_arrived, k-distance); (node, k+1). total edge: e * cnt, ma: node * (cnt+1) + k
        base = cnt + 1
        min_times = [INF for _ in range(n * base)]
        hq = [[0, start*base]]
        heapq.heapify(hq)
        target = end * base
        while True:
            t, idx = heapq.heappop(hq)
            node, rm_charge = idx // base, idx % base
            min_times[idx] = min(min_times[idx], t)
            if idx == target:
                return t
            if rm_charge < cnt: # chargeable
                heapq.heappush(hq, [t + charge[node], idx + 1])
            for nodeN, d in edges[node]:
                if d <= rm_charge: # can arrive to nodeN
                    idxN = nodeN * base + rm_charge - d
                    if min_times[idxN] == INF:
                        heapq.heappush(hq, [t + d, idxN])

