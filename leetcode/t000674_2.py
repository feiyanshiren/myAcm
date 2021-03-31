from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = anchor = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]: anchor = i
            ans = max(ans, i - anchor + 1)
        return ans



s = Solution()
print(s.findLengthOfLCIS([1,3,5,4,7]))
print(s.findLengthOfLCIS([2,2,2,2,2]))