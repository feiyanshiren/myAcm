import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return num == 6 or num == 28 or num == 496 or num == 8128 or num == 33550336
            
    
s = Solution()
import time
t = time.time()
for i in range(9999):
    print(s.checkPerfectNumber(i))
print(time.time() - t)
"""
print(s.checkPerfectNumber(28))
print(s.checkPerfectNumber(100000000))
print(s.checkPerfectNumber(99999999))
print(s.checkPerfectNumber(1))
print(s.checkPerfectNumber(2))
"""