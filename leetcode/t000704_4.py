from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            return -1

    
s = Solution()
import time
t = time.time()
for i in range(100000):
    print(s.search([-1,0,3,5,9,12], 9))
    print(s.search( [-1,0,3,5,9,12], 2))

print(time.time() - t)
