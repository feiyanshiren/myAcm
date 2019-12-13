from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = len(nums)
        if l == 1:
            return 0
        if l == 2:
            if abs(nums[1] - nums[0]) == 1:
                return 2
            else:
                return 0
        m = {}
        for i in nums:
            m[i] = m.get(i, 0) + 1
        a = sorted(m.items(), key=lambda x: x[0])
        mx = 0
        for i in range(len(a) - 1):
            a1 = a[i]
            a2 = a[i + 1]
            if abs(a1[0] - a2[0]) == 1:
                mx = max(mx, a1[1] + a2[1])
        return mx





s = Solution()
print(s.findLHS([1,3,2,2,5,2,3,7]))
