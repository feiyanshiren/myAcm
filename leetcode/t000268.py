class Solution:
    def missingNumber(self, nums) -> int:
        if nums == None or len(nums) == 0:
            return 0
        nums.sort()
        l = len(nums)
        if nums[-1] != l:
            return l
        elif nums[0] != 0:
            return 0
        for i in range(1, l):
            e = nums[i - 1] + 1
            if nums[i] != e:
                return e
        return -1
    
s = Solution()
print(s.missingNumber([2]))
# print(s.missingNumber([3,0,1]))
# print(s.missingNumber([9,6,4,2,3,5,7,0,1]))
# print(s.missingNumber([]))
# print(s.missingNumber(None))
# print(s.missingNumber([0]))
