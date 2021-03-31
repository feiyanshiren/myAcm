from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        a = sorted(nums)
        s = l + 1
        e = -1
        for i in range(len(nums)):
            if nums[i] != a[i]:
                s = min(s, i)
                e = max(e, i)
        return e + 1 - s if e != -1 else 0

s = Solution()
print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
