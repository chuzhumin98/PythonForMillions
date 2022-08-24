class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        step = 0
        s_pred = s
        while True:
            s_new = s_pred.replace('01', '10')
            if s_pred == s_new:
                break
            else:
                step += 1
                s_pred = s_new
        return step