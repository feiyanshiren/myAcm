from typing import List
import time
# from memory_profiler import profile
from guppy import hpy 

class Solution:
    # @profile
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)
    

a = []
for i in range(21474):
    a.append(i)
t = time.time()
s = Solution()
print(s.minMoves(a)) 
print(time.time() - t)
h = hpy()
print(h.heap())
