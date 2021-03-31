# -*- coding: utf-8 -*-
# 排序法
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums) // 2]
    

s = Solution()
print(s.majorityElement([1, 2, 3, 3, 3]))
print(s.majorityElement([3,2,3]))
print(s.majorityElement([2,2,1,1,1,2,2]))