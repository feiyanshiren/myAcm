from functools import lru_cache
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(nums, key=lru_cache(None)(lambda n: (nums.count(n), -n)))


s = Solution()
print(s.frequencySort([1, 1, 2, 2, 2, 3]))
print(s.frequencySort([2, 3, 1, 3, 2]))
print(s.frequencySort([-1, 1, -6, 4, 5, -6, 1, 4, 1]))
