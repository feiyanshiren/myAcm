class Solution:
    def missingNumber(self, nums) -> int:
        l = len(nums)
        e = l * (l + 1) // 2
        a = sum(nums)
        return e - a
      
    
s = Solution()
print(s.missingNumber([2]))
print(s.missingNumber([3,0,1]))
print(s.missingNumber([9,6,4,2,3,5,7,0,1]))
# print(s.missingNumber([]))
# print(s.missingNumber(None))
# print(s.missingNumber([0]))
