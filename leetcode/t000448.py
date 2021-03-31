from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        a = []
        n = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in n:
                a.append(i)
        return a
    
s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))