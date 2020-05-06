from typing import List
import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a = bisect.bisect_left(nums, target)
        return -1 if a >= len(nums) or nums[a] != target else a

    
s = Solution()
"""
import time
t = time.time()
for i in range(100000):
    print(s.search([-1,0,3,5,9,12], 9))
    print(s.search( [-1,0,3,5,9,12], 2))

print(time.time() - t)
"""
print(s.search([-1,0,3,5,9,12],13))
