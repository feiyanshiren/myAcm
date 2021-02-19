from typing import List
import collections


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        map_nums = dict(collections.Counter(nums))
        sort_map = sorted(map_nums.items(), key=lambda x: (x[1], -x[0]))
        return sum([[x[0]] * x[1] for x in sort_map], [])


s = Solution()
print(s.frequencySort([1, 1, 2, 2, 2, 3]))
print(s.frequencySort([2, 3, 1, 3, 2]))
print(s.frequencySort([-1, 1, -6, 4, 5, -6, 1, 4, 1]))
