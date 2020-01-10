from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        d = -1
        m = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                d = nums[i]
            elif nums[i] > nums[i - 1] + 1:
                m = nums[i - 1] + 1
        l = len(nums)
        return [d, l if nums[l - 1] != l else m]

s = Solution()
print(s.findErrorNums([1,2,2,4]))

"""
使用排序
"""