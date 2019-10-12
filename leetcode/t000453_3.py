from typing import List
import time
from memory_profiler import profile
# from guppy import hpy

class Solution:
    @profile
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        s = sum(nums)
        m = nums[0]
        l = len(nums)
        return s - m * l
    
a = []
for i in range(21474):
    a.append(i)
t = time.time()
s = Solution()
print(s.minMoves(a)) 
print(time.time() - t)
# h = hpy()
# print(h.iso(s.minMoves(a)))
