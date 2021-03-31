from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        xor = 0
        xor0 = 0
        xor1 = 0
        for n in nums:
            xor ^= n
        l = len(nums)
        for i in range(1, l + 1):
            xor ^= i
        rightmostbit = xor & ~(xor -1)
        for n in nums:
            if (n & rightmostbit) != 0:
                xor1 ^= n
            else:
                xor0 ^= n
        for i in range(1, l + 1):
            if (i & rightmostbit) != 0:
                xor1 ^= i
            else:
                xor0 ^= i
        for i in range(1, l):
            if nums[i] == xor0:
                return [xor0, xor1]
        return [xor1, xor0]
        

s = Solution()
print(s.findErrorNums([1,1]))

"""
使用异或运算
"""