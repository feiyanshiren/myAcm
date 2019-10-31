from typing import List

class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        m = {0: "Gold Medal", 1: "Silver Medal", 2: "Bronze Medal"}
        a = nums[::]
        a.sort(reverse=True)
        b = {v: k for k, v in enumerate(a)}
        return [m.get(b.get(i), str(b.get(i) + 1)) for i in nums]

s = Solution()
print(s.findRelativeRanks([5, 4, 3, 2, 1]))
