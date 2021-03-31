from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True
        if not flowerbed:
            return False
        ll = len(flowerbed)
        if n > ll // 2 + 1:
            return False
        for i in range(ll):
            im = flowerbed[i]
            il = 0 if i == 0 else flowerbed[i - 1]
            ir = 0 if i == ll - 1 else flowerbed[i + 1]
            if im == 0 and il == 0 and ir == 0:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    break
        return n == 0
        


s = Solution()
print(s.canPlaceFlowers([1,0,0,0,1], 1))
print(s.canPlaceFlowers([1,0,0,0,1], 2))