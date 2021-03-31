import math
import time

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        r = set([1])
        k = int(math.sqrt(num))
        for i in range(2, k):
            if num % i == 0:
                r.add(i)
                r.add(num // i)
        if k ** 2 == num:
            r.add(k)
        return sum(r) == num
            
    
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