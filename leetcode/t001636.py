from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        map_nums = {}
        for i in nums:
            map_nums[i] = map_nums.get(i, 0) + 1
        sort_map = sorted(map_nums.items(), key=lambda x: (x[1], -x[0]))
        res = []
        for i in sort_map:
            for j in range(i[1]):
                res.append(i[0])
        return res


s = Solution()
print(s.frequencySort([1, 1, 2, 2, 2, 3]))
print(s.frequencySort([2, 3, 1, 3, 2]))
print(s.frequencySort([-1, 1, -6, 4, 5, -6, 1, 4, 1]))
