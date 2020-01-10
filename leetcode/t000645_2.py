from typing import List
from collections import Counter


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a = dict(Counter(nums))
        d = -1
        m = 1
        for i in range(1, len(nums) + 1):
            b = a.get(i, 0)
            if b == 2:
                d = i
            elif b == 0:
                m = i
        return [d, m]
        

s = Solution()
print(s.findErrorNums([1,1]))

"""
使用map，可以使用Counter
"""