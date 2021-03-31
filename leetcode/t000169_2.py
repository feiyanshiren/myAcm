# -*- coding: utf-8 -*-
# 摩尔投票法
class Solution:
    def majorityElement(self, nums):
        n = nums[0]
        c = 1
        l = len(nums)
        for i in range(1, l):
            if c == 0:
                n = nums[i]
            if n == nums[i]:
                c += 1
            else:
                c -= 1
        return n 
    

s = Solution()
print(s.majorityElement([1, 2, 3, 3, 3]))
print(s.majorityElement([3,2,3]))
print(s.majorityElement([2,2,1,1,1,2,2]))