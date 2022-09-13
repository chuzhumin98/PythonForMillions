from typing import List
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        adict = dict()
        for a, b in knowledge:
            adict[a] = b
        items = s.split('(')
        s_out = items[0]
        for item in items[1:]:
            key, content = item.split(')')
            s_out += adict.get(key, '?')
            s_out += content
        return s_out