from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = 0
        for i in range(k):
            s += nums[i]
        r = s
        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            r = max(r, s)
        return r / k


s = Solution()
print(s.findMaxAverage([1,12,-5,-6,50,3], 4))

