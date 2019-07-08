class Solution:
    def robTo(self, nums, last):
        if last == 0:
            return nums[0]
        s1 = 0
        if last - 2 >= 0:
            s1 = self.robTo(nums, last - 2) + nums[last]
        else:
            s1 = nums[last]
        s2 = self.robTo(nums, last - 1)
        return max(s1, s2)
        
    def rob(self, nums):
        return self.robTo(nums, len(nums) - 1);
   
s = Solution()
print(s.rob([1, 2, 3, 1]))
print(s.rob([2, 7, 9, 3, 1]))
print(s.rob([1, 3, 1, 3, 100])) 
