class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
                        除K取余法
        """
        a = 0
        while n:
            a += n % 2
            n >>= 1
        return a
    
s = Solution()
print(s.hammingWeight(9999999999))