import math
class Solution:
    def countPrimes(self, n):
        if n < 3:
            return 0
        m = [1] * n
        m[0], m[1] = 0, 0
        for i in range(2, int(math.sqrt(n)) + 1):
            if m[i]:
                m[i*i:n:i] = [0] * len(m[i*i:n:i])
        return sum(m)
        
        
s = Solution()
print(s.countPrimes(10000))