from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        k = {}
        s = []
        for i in nums2[::-1]:
            while len(s) != 0 and s[-1] <= i:
                s.pop()
            if len(s) == 0:
                k[i] = -1
                # res.insert(0, -1)
            else:
                # res.insert(0, s[-1])
                k[i] = s[-1]
            s.append(i)
        # print(k)
        for i in nums1:
            res.append(k[i])
        return res
    
s = Solution()
print(s.nextGreaterElement([4,1,2], [1,3,4,2]))
print(s.nextGreaterElement([2,4], [1,2,3,4]))