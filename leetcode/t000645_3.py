from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = -1
        m = 1
        for i in nums:
            if nums[abs(i) - 1] < 0:
                d = abs(i)
            else:
                nums[abs(i) - 1] *= -1
        for i in range(1, len(nums)):
            if nums[i] > 0:
                m = i + 1
        return [d, m]
        

s = Solution()
print(s.findErrorNums([1,1]))

"""
使用负数标记
"""