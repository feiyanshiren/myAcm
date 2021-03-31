from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        elif l == 1:
            return 1
        else:
            c = 0
            d = 0
            for i in range(l - 1):
                if nums[i + 1] > nums[i]:
                    d += 1
                else:
                    d += 1
                    c = max(c, d)
                    d = 0
            if d != 0:
                d += 1
                c = max(c, d)
            return c



s = Solution()
print(s.findLengthOfLCIS([1,3,5,4,7]))
print(s.findLengthOfLCIS([2,2,2,2,2]))