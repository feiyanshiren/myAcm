from typing import List

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        r1 = len(nums)
        if r1 == 0:
            return nums
        c1 = len(nums[0])
        if r * c != r1 * c1:
            return nums
        a = []
        res = []
        for i in nums:
            for j in i:
                a.append(j)
        for i in range(r):
            b = []
            for j in range(c):
                b.append(a.pop(0))
            res.append(b)
        return res
    
s = Solution()
print(s.matrixReshape([[1,2],[3,4]], 1, 4))
print(s.matrixReshape([[1,2],[3,4]], 2, 4))
