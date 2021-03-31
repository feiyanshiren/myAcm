from typing import List

"""
对于每个房屋，要么用前面的暖气，要么用后面的，二者取近的，得到距离；
对于所有的房屋，选择最大的上述距离。
"""

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        l1 = len(houses)
        l2 = len(heaters)
        if l2 == 1:
            return max(abs(houses[0] - heaters[0]), abs(houses[-1] - heaters[0]))
        res = 0
        a = 0
        b = l1 - 1
        while b >= 0 and houses[b] >= heaters[-1]:
            b -= 1
        if b != l1 - 1:
            res = houses[-1] - heaters[-1]
        c = 0
        while c < l1 and houses[c] <= heaters[0]:
            c += 1
        if c != 0:
            res = max(res, heaters[0] - houses[0] )
        for i in range(c, b + 1):
            while houses[i] > heaters[a]:
                a += 1
            if houses[i] == heaters[a]:
                continue
            res = max(res, min(houses[i] - heaters[a - 1], heaters[a] - houses[i]))
        return res
            
            
    
s = Solution()
print(s.findRadius( [1,2,3],[2]))
print(s.findRadius( [1,2,3,4],[1,4]))