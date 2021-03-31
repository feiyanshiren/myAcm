from typing import List

class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        l1 = len(M)
        l2 = len(M[0])
        b = [[0] * l2 for _ in M]
        for i in range(l1):
            for j in range(l2):
                a = [M[i][j]]
                if i - 1 >= 0:
                    a.append(M[i - 1][j])
                if i + 1 < l1:
                    a.append(M[i + 1][j])
                if j - 1 >= 0:
                    a.append(M[i][j - 1])
                if j + 1 < l2:
                    a.append(M[i][j + 1])
                if i - 1 >= 0 and j - 1 >= 0:
                    a.append(M[i - 1][j - 1])
                if i - 1 >= 0 and j + 1 < l2:
                    a.append(M[i - 1][j + 1])
                if i + 1 < l1 and j + 1 < l2:
                    a.append(M[i + 1][j + 1])
                if i + 1 < l1 and j - 1 >= 0:
                    a.append(M[i + 1][j - 1])
                b[i][j] = sum(a) // len(a)
        return b



s = Solution()
print(s.imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))

