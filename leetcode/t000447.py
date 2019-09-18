from typing import List

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        s = 0
        for i in points:
            m = {}
            for j in points:
                if i != j:
                    d = (i[0] - j[0]) ** 2 + (i[1] -  j[1]) ** 2
                    m[d] = m.get(d, 0) + 1
            for k, v in m.items():
                if v >= 2:
                    s += v * (v - 1)
        return s
    
s = Solution()
print(s.numberOfBoomerangs([[0,0],[1,0],[2,0]]))
print(s.numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]]))