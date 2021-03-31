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
        mx = 0
        for k, v in m.items():
            k2 = k + 1
            if k2 in m:
                mx = max(mx, v + m[k2])
        return mx





s = Solution()
print(s.findLHS([1,3,2,2,5,2,3,7]))