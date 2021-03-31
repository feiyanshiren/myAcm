from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = nums[:]
        l = len(nums)
        for i in range(1, l):
            n[i] = n[i - 1] + nums[i]
        r = n[k - 1] / k
        for i in range(k, l):
            r = max(r, (n[i] - n[i - k]) / k)
        return r


s = Solution()
print(s.findMaxAverage([1,12,-5,-6,50,3], 4))

