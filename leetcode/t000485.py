from typing import List
import re

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ma = 0
        te = 0
        for i in nums:
            if i == 1:
                te += 1
            else:
                ma = max(ma, te)
                te = 0
        ma = max(ma, te)
        return ma
    

s = Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))

"""
a = "110111"
b = re.findall("1+", a)
print(b)
"""