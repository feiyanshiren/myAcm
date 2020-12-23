from collections import Counter
from typing import List



class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        l1 = len(mat)
        l2 = len(mat[0])
        m = []
        n = []
        for i in range(l1):
            for j in range(l2):
                if mat[i][j] == 1:
                    m.append(i)
                    n.append(j)
        res = 0
        m2 = [v[0] for v in Counter(m).most_common() if v[1] == 1]
        n2 = [v[0] for v in Counter(n).most_common() if v[1] == 1]
        for i in m2:
            if n[m.index(i)] in n2:
                res += 1
        return res


s = Solution()
# print(s.numSpecial([[1, 0, 0], [0, 0, 1], [1, 0, 0]]))
# print(s.numSpecial([[1, 0, 0],[0, 1, 0],[0, 0, 1]]))
#
# print(s.numSpecial([[0, 0, 0, 1],[1, 0, 0, 0],[0, 1, 1, 0],[0, 0, 0, 0]]))
#
# print(s.numSpecial([[0, 0, 0, 0, 0],[1, 0, 0, 0, 0],[0, 1, 0, 0, 0],[0, 0, 1, 0, 0],[0, 0, 0, 1, 1]]))
#
# print(s.numSpecial([[1, 0, 0], [0, 0, 1]]))

print(s.numSpecial([[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,1],[0,0,0,0,1,0,0,0],[1,0,0,0,1,0,0,0],[0,0,1,1,0,0,0,0]]))

# print(s.numSpecial([[0,0,0,0,0,0,0,0],
#                     [0,1,0,0,0,0,0,0],
#                     [0,0,0,0,0,0,0,0],
#                     [0,0,0,0,0,0,0,0],
#                     [1,0,0,0,0,0,0,1],
#                     [0,0,0,0,0,0,1,0],
#                     [0,0,0,0,0,0,0,1]]))
