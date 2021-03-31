from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        a = [0 for i in range(20001)]
        l = 10000
        for n in nums:
            a[n + l] += 1
        d = 0
        s = 0
        for i in range(-10000, 10001):
            s += (a[i + l] + 1 - d) // 2 * i
            d = (2 + a[i + l] - d) % 2
        return s
    
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
