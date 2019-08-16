from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m1 = {}
        for i in nums1:
            m1[i] =  m1.get(i, 0) + 1
        res = []
        for i in nums2:
            if m1.get(i, 0) != 0:
                res.append(i)
                m1[i] -= 1
        return res
      
                
    
s = Solution()
print(s.intersect([1, 2, 2, 1], [2, 2]))
print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
