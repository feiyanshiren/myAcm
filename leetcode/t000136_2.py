# 异或：相同为0，不同为1. 异或同一个数两次，原数不变。
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for num in nums:
            a = a ^ num
        return a

s = Solution()
print(s.singleNumber([2, 2, 1]))
print(s.singleNumber([4, 1, 2, 1, 2]))


