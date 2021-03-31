from typing import List

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return min(len(candies) // 2, len(set(candies)))

s = Solution()
print(s.distributeCandies([1,1,2,2,3,3]))
print(s.distributeCandies([1,1,2,3]))