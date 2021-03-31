class Solution:
    def missingNumber(self, nums) -> int:
        m = len(nums)
        for i in range(len(nums)):
            m ^= i ^ nums[i]
        return m
      
    
s = Solution()
print(s.missingNumber([2]))
# print(s.missingNumber([3,0,1]))
# print(s.missingNumber([9,6,4,2,3,5,7,0,1]))
# print(s.missingNumber([]))
# print(s.missingNumber(None))
# print(s.missingNumber([0]))
