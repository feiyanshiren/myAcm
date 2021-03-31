from typing import List

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if not n:
            return True
        if not flowerbed:
            return False
        ll = len(flowerbed)
        if n > ll // 2 + 1:
            return False
        flowerbed = [0]+flowerbed+[0]
        for i in range(1, ll + 1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1  
                n -= 1
                if n == 0:
                    break
        return n == 0   

s = Solution()
print(s.canPlaceFlowers([1,0,0,0,1], 1))
print(s.canPlaceFlowers([1,0,0,0,1], 2))