from typing import List

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        import numpy as np
        try:
            nums = np.array(nums).reshape(r,c)
            l = []
            for i in range(r):
                l.append(list(nums[i]))
            return l
        except ValueError:
            return nums

    
s = Solution()
print(s.matrixReshape([[1,2],[3,4]], 1, 4))
print(s.matrixReshape([[1,2],[3,4]], 2, 4))
