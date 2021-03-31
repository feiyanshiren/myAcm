from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 0
        self.the_list = [0] * n
        self.n = n


    def insert(self, idKey: int, value: str) -> List[str]:
        self.the_list[idKey - 1] = value
        res = []
        if (idKey - 1) == self.ptr:
            while self.ptr < self.n and self.the_list[self.ptr] != 0:
                res.append(self.the_list[self.ptr])
                self.ptr += 1
        return res




# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
# ----2

class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.the_map = {}
        self.n = n


    def insert(self, idKey: int, value: str) -> List[str]:
        self.the_map[idKey] = value
        res = []
        if idKey == self.ptr:
            while self.ptr <= self.n and self.the_map.get(self.ptr, 0) != 0:
                res.append(self.the_map[self.ptr])
                self.ptr += 1
        return res