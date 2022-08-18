from typing import List
class OrderedStream:

    def __init__(self, n: int):
        self.N = n
        self.data = [None for _ in range(n)]
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.data[idKey-1] = value
        alist = []
        while True:
            if self.ptr >= self.N:
                break
            if self.data[self.ptr] is None:
                break
            alist.append(self.data[self.ptr])
            self.ptr += 1
        return alist



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)