from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = 0
        l = len(nums)
        if l == 2:
            return False
        for i in range(l):
            n = nums[i]
            for j in range(l):
                m = nums[j]
                if i != j and n == m:
                    if abs(i - j) <= k:
                        return True
        return False
    
s = Solution()
print(s.containsNearbyDuplicate([], 0))
print(s.containsNearbyDuplicate([1, 2, 3, 1], 3))
print(s.containsNearbyDuplicate([1, 0, 1, 1], 1))
print(s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
