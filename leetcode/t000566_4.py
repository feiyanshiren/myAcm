from typing import List

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums)*len(nums[0])!=r*c:
            return nums
        l=[]
        new=[]
        for i in range(len(nums)):
            l+=nums[i]
        for i in range(0,len(l),c):
            new.append(l[i:i+c])
        return new

s = Solution()
print(s.matrixReshape([[1,2],[3,4]], 1, 4))
print(s.matrixReshape([[1,2],[3,4]], 2, 4))