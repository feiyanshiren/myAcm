import math
class Solution:
    def isPrime(self, n):
        if n < 3:
            return n > 1
        if n % 2 == 0:
            return False
        s = int(math.sqrt(n) + 1)
        for i in range(3, s + 1, 2):
            if n % i == 0:
                return False
        return True

    def countPrimes(self, n):
        if n < 3:
            return 0
        c = 0
        for i in range(2, n):
            if self.isPrime(i):
                c += 1
        return c
        
s = Solution()
print(s.countPrimes(10000))