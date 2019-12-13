from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        m = [[0 for i in range(n)] for j in range(m)]
        for i in ops:
            for j in range(i[0]):
                for k in range(i[1]):
                    m[j][k] += 1
            print(m)
        mx = m[0][0]
        mcount = 0
        for i in m:
            for j in i:
                if j == mx:
                    mcount += 1
        return mcount

s = Solution()
print(s.maxCount(3, 3, [[2, 2], [3, 3]]))