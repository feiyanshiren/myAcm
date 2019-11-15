from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        res = 0
        nums.sort()
        i = 0
        j = 1
        
        while j < len(nums):
            if abs(nums[i] - nums[j]) < k:
                j += 1
                continue
            if abs(nums[i] - nums[j]) == k and i != j and nums[i] != nums[i - 1]:
                res += 1
            
            i += 1
            j = i + 1
            
        return res
    
s = Solution()
print(s.findPairs([3, 1, 4, 1, 5], 2))
print(s.findPairs([1, 2, 3, 4, 5], 1))
print(s.findPairs([1, 3, 1, 5, 4], 0))