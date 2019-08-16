from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = set()
        b = set()
        for i in nums1:
            a.add(i)
        for i in nums2:
            b.add(i)
        return list(a & b)
    
s = Solution()
print(s.intersection([1, 2, 2, 1], [2, 2]))
print(s.intersection([4, 9, 5], [9, 4, 9, 8, 4]))