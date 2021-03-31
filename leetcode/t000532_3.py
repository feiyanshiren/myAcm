from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        return len({nums[i] for i in range(len(nums)) if nums[i] + k in nums[i + 1:]}) if k >= 0 else 0
    
s = Solution()
print(s.findPairs([3, 1, 4, 1, 5], 2))
print(s.findPairs([1, 2, 3, 4, 5], 1))
print(s.findPairs([1, 3, 1, 5, 4], 0))