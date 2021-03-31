from typing import List
import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        a = math.sqrt(area)
        if int(a) ** 2 == area:
            return [int(a), int(a)]
        else:
            if self.isPrime(area):
                return [area, 1]
            else:
                b = int(a)
                while area % b != 0:
                    if b == 1:
                        return [area, 1]
                    else:
                        b -= 1
                return [area // b, b]
                    
    
    def isPrime(self, n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
s = Solution()
print(s.constructRectangle(4))
print(s.constructRectangle(9999999999))