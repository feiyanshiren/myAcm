from typing import List

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        candies.sort()
        c = 1
        i = 1
        while i < len(candies) and c < len(candies) // 2:
            if candies[i] > candies[i - 1]:
                c += 1
            i += 1
        return c

s = Solution()
print(s.distributeCandies([1,1,2,2,3,3]))
print(s.distributeCandies([1,1,2,3]))