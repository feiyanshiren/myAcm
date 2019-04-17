class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        f = 1 if x >= 0 else -1
        rev = 0
        d = abs(x)
        while d != 0:
            pop = d % 10
            d = d // 10
            if rev > 2147483647 // 10 or (rev == 2147483647 // 10 and pop > 7):
                return 0
            if rev < -2147483648 // 10 or (rev == -2147483648 // 10 and pop < -8):
                return 0
            rev = rev * 10 + pop
        return rev * f


s = Solution()
print(s.reverse(-120))
