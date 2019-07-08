class Solution:
    def rob(self, nums):
        a = 0
        b = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                a += nums[i]
                a = max(a, b)
            else:
                b += nums[i]
                b = max(a, b)
        return max(a, b)
   
s = Solution()
print(s.rob([1, 2, 3, 1]))
print(s.rob([2,7,9,3,1])) 
print(s.rob([1, 3, 1, 3, 100])) 
