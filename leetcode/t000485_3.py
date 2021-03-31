from typing import List
import re

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a = str(nums)[1:-1].replace(", ", "").rstrip()
        b = a.split("0")
        ma = 0
        for i in b:
            ma = max(len(i), ma)
        return ma

s = Solution()
print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))
print(s.findMaxConsecutiveOnes([]))
print(s.findMaxConsecutiveOnes([0]))
print(s.findMaxConsecutiveOnes([1]))

"""
a = "110111"
b = re.findall("1+", a)
print(b)
"""