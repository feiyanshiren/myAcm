class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [0, 1]
        nums += [0] * (n - 1)
        for i in range(n + 1):
            if 2 <= 2 * i <= n:
                nums[2 * i] = nums[i]
            if 2 <= 2 * i + 1 <= n:
                nums[2 * i + 1] = nums[i] + nums[i + 1]
        print(nums)
        return max(nums)

    def getMaximumGenerated2(self, n: int) -> int:
        nums = [0, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
                9, 9, 11, 11, 11, 11, 11, 11, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13,
                13, 13, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 15, 15, 18, 18, 18, 18, 18, 18, 18, 18, 19, 19, 21, 21,
                21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21]
        return nums[n]


s = Solution()
print(s.getMaximumGenerated2(7))
print(s.getMaximumGenerated2(2))
print(s.getMaximumGenerated2(3))
