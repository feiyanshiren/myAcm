class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1.extend(nums2)
        nums1.sort()
        while 0 in nums1:
            nums1.remove(0)


s = Solution()
a = [1,1,2,3,4,5]
b = [2,6,7]
s.merge(a, 6, b, 3)
print(a)

a = [1,2,3,0,0,0]
b = [2,5,6]
s.merge(a, 3, b, 3)
print(a)