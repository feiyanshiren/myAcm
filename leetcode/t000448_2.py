from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)
        nums = set(nums)
        for i in range(1, l + 1):
            if i in nums:
                nums.remove(i)
            else:
                nums.add(i)
        return list(nums)
    
s = Solution()
print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))