from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ll = len(flowerbed)
        for i in range(ll):
            im = flowerbed[i]
            il = 0 if i == 0 else flowerbed[i - 1]
            ir = 0 if i == ll - 1 else flowerbed[i + 1]
            if im == 0 and il == 0 and ir == 0:
                flowerbed[i] = 1
                n -= 1
        return n == 0