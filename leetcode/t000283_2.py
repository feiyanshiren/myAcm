class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        a = len(nums)
        for i in range(a):
            if nums[i] != 0:
                nums[l] = nums[i]
                l += 1
        
        for i in range(l, a):
            nums[i] = 0
                
    

s = Solution()
n = [0,1,0,3,12]
# n = [1,3,12,0,0]
s.moveZeroes(n)
print(n)


        