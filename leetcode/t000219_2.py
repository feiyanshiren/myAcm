from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        if l == 0:
            return False
        m = {}
        for i in range(l):
            if nums[i] in m and i - m[nums[i]] <= k:
                return True
            m[nums[i]] = i
        return False
    
s = Solution()
print(s.containsNearbyDuplicate([], 0))
print(s.containsNearbyDuplicate([1, 2, 3, 1], 3))
print(s.containsNearbyDuplicate([1, 0, 1, 1], 1))
print(s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
