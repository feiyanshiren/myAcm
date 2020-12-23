from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        l1 = len(mat)
        l2 = len(mat[0])
        res = 0
        for i in range(l1):
            for j in range(l2):
                if mat[i][j] == 1:
                    t = 0
                    for k in range(l1):
                        if k != i:
                            if mat[k][j] == 1:
                                t = 1
                                break
                    for k in range(l2):
                        if k != j:
                            if mat[i][k] == 1:
                                t = 1
                                break
                    if t == 0:
                        res += 1
        return res


s = Solution()
print(s.numSpecial([[1, 0, 0], [0, 0, 1], [1, 0, 0]]))
print(s.numSpecial([[1, 0, 0],[0, 1, 0],[0, 0, 1]]))

print(s.numSpecial([[0, 0, 0, 1],[1, 0, 0, 0],[0, 1, 1, 0],[0, 0, 0, 0]]))

print(s.numSpecial([[0, 0, 0, 0, 0],[1, 0, 0, 0, 0],[0, 1, 0, 0, 0],[0, 0, 1, 0, 0],[0, 0, 0, 1, 1]]))

print(s.numSpecial([[1, 0, 0], [0, 0, 1]]))

print(s.numSpecial([[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,1],[0,0,0,0,1,0,0,0],[1,0,0,0,1,0,0,0],[0,0,1,1,0,0,0,0]]
))

