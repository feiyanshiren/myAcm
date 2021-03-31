from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        m = {}
        res = 0
        for i in nums:
            m[i] = m.get(i, 0) + 1
        if k == 0:
            for k, v in m.items():
                if v > 1:
                    res += 1
        else:
            for i in m:
                if m.get(i + k, 0) != 0:
                    res += 1
        return res
    
s = Solution()
print(s.findPairs([3, 1, 4, 1, 5], 2))
print(s.findPairs([1, 2, 3, 4, 5], 1))
print(s.findPairs([1, 3, 1, 5, 4], 0))