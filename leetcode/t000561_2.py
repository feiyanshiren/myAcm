from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
    
s = Solution()
import time
t = time.time()
for i in range(1000):
    print(s.arrayPairSum([1, 4, 3, 2]))
print(s.arrayPairSum([1, 1]))
print(s.arrayPairSum([-1, 3, -4,-5]))
print(s.arrayPairSum([-1, -4, -6,-7]))
print(s.arrayPairSum([1,2,0,-3]))
print(time.time() - t)