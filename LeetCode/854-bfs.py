###
# Solution: bfs
# we use bfs to solve this problem, for each time, when we consider a k-step modify string s, we need to
# conduct swap to make the smallest s[i] != s2[i] to become equivalent, that is trying to swap i and each j such
# that s[j] = s2[i], then we just use bfs to find the min swap times
###
import collections
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        fs = {s1: 0}
        n = len(s1)
        dq = collections.deque()
        dq.append([s1, 0, 0])  # s, step, idx
        while len(dq) > 0:
            s, step, idx = dq.popleft()
            while idx < n:
                if s[idx] != s2[idx]:
                    break
                idx += 1
            if idx == n:
                return step
            for i in range(idx + 1, n):
                if s[i] == s2[idx]:
                    snew = s[:idx] + s[i] + s[idx + 1:i] + s[idx] + s[i + 1:]
                    if snew not in fs:
                        fs[snew] = step + 1
                        dq.append([snew, step + 1, idx + 1])


