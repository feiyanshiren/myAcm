import math
import time

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        s = 1
        k = int(math.sqrt(num))
        for i in range(2, k):
            if num % i == 0:
                s += i + num // i
        if k ** 2 == num:
            s += k
        return s == num
            


s = Solution()
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

# print(99999999 // 10001)