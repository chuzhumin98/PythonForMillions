class Solution:
    def get_split(self, s):
        ss, snums = [], []
        if len(s) == 0:
            return ss, snums
        else:
            ss.append(s[0])
            snums.append(1)
            for char in s[1:]:
                if char == ss[-1]:
                    snums[-1] += 1
                else:
                    ss.append(char)
                    snums.append(1)
            return ss, snums

    def expressiveWords(self, s: str, words: List[str]) -> int:
        ss0, snums0 = self.get_split(s)
        ss0_join = ''.join(ss0)
        _sum = 0
        for word in words:
            ssw, snumsw = self.get_split(word)
            if ss0_join == ''.join(ssw):
                deltas = sum([1 if snums0[i] == snumsw[i] or (snums0[i] >= 3 and snums0[i] >= snumsw[i]) else 0 for i in range(len(snums0))])
                if deltas == len(snums0):
                    _sum += 1
        return _sum