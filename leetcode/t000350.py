from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        d = []
        for i in range(len(nums1)):
            n1 = nums1[i]
            for j in range(len(nums2)):
                n2 = nums2[j]
                if n1 == n2 and j not in d:
                    d.append(j)
                    res.append(n1)
                    break
        return res
    
s = Solution()
print(s.intersect([1, 2, 2, 1], [2, 2]))
print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
