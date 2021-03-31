from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        l2 = len(nums2)
        for i in nums1:
            a = nums2.index(i)
            c = 0
            for j in range(a + 1, l2):
                b = nums2[j]
                if b > i:
                    c = 1
                    res.append(b)
                    break
            if c == 0:
                res.append(-1)
        return res
    
s = Solution()
print(s.nextGreaterElement([4,1,2], [1,3,4,2]))
print(s.nextGreaterElement([2,4], [1,2,3,4]))