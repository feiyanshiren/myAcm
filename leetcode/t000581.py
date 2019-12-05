from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l = len(nums)
        a = nums[:]
        a.sort()
        s = -1
        e = -1
        for i in range(l):
            if nums[i] != a[i]:
                s = i
                break
        for i in range(l - 1, -1, -1):
            if nums[i] != a[i]:
                e = i
                break
        if s == -1 or e == -1:
            return 0
        return e + 1 - s

s = Solution()
print(s.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
