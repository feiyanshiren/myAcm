class Solution:
    def rotate(self, nums, k) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        d = l - ( k % l)
        b = nums[d:] + nums[:d]
        nums.clear()
        nums += b
        
s = Solution()
m = [1,2,3,4,5,6,7]
s.rotate(m, 3)
print(m)