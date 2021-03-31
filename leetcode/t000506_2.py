from typing import List

class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        b = {v: str(k + 1) for k, v in enumerate(sorted(nums, reverse=True))}
        return [{"1": "Gold Medal", "2": "Silver Medal", "3": "Bronze Medal"}.get(b.get(i), b.get(i)) for i in nums]

s = Solution()
print(s.findRelativeRanks([5, 4, 3, 2, 1]))