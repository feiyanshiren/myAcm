from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        S = sum(set(nums))
        return [sum(nums)-S ,len(nums)*(len(nums)+1)//2-S]
        

s = Solution()
print(s.findErrorNums([1,1]))

"""
数学方法，求1+2...+N的和，nums唯一set()的和，和nums的和对应做减法直接得到结果
"""