from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m+n] = nums2      # 将nums2合并到nums1中
        nums1.sort()              # 直接使用内置排序方法sort


s = Solution()
a = [1,1,2,3,4,5]
b = [2,6,7]
s.merge(a, 6, b, 3)
print(a)

a = [1,2,3,0,0,0]
b = [2,5,6]
s.merge(a, 3, b, 3)
print(a)