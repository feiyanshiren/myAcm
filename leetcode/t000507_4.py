import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num % 2 != 0:
            return False
        i = 2
        s = 1
        while i < num // i:
            if num % i == 0:
                s += i + num // i
            i += 1
        return s == num
            
        
            
    
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