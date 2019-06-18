class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = k % len(nums)
        nums[:] = nums[-d:] + nums[:-d]
        
s = Solution()
m = [1,2,3,4,5,6,7]
s.rotate(m, 3)
print(m)