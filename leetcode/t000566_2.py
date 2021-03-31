from typing import List

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        try:
            a = [j for i in nums for j in i]
            return [[a.pop(0) for j in range(c)] for i in range(r)]
        except:
            return nums
    
s = Solution()
print(s.matrixReshape([[1,2],[3,4]], 1, 4))
print(s.matrixReshape([[1,2],[3,4]], 2, 4))
