class Solution:
    def missingNumber(self, nums) -> int:
        a = set()
        for i in nums:
            a.add(i)
        for i in range(len(nums) + 1):
            if i not in a:
                return i
        return -1
      
    
s = Solution()
print(s.missingNumber([2]))
# print(s.missingNumber([3,0,1]))
# print(s.missingNumber([9,6,4,2,3,5,7,0,1]))
# print(s.missingNumber([]))
# print(s.missingNumber(None))
# print(s.missingNumber([0]))
