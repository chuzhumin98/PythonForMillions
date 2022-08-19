from typing import List
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        node1_set = set([node1])
        node2_set = set([node2])
        _step = 0
        c1, c2 = node1, node2
        if c1 == c2:
            return c1

        while True:
            _step += 1
            finish_num = 0
            c1_next = edges[c1]
            ans = []
            if c1_next == -1 or c1_next in node1_set:
                finish_num += 1
            else:
                if c1_next in node2_set:
                    ans.append(c1_next)
                node1_set.add(c1_next)
                c1 = c1_next

            c2_next = edges[c2]
            if c2_next == -1 or c2_next in node2_set:
                finish_num += 1
            else:
                if c2_next in node1_set:
                    ans.append(c2_next)
                node2_set.add(c2_next)
                c2 = c2_next