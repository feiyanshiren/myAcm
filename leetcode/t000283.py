class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        l = len(nums)
        while i != l:
            k = nums[i]
            if k == 0:
                nums.append(k)
                nums.pop(i)
                l -= 1
            else:
                i += 1
                
    

s = Solution()
# n = [0,1,0,3,12]
n = [1,3,12,0,0]
s.moveZeroes(n)
print(n)


        