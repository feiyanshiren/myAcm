class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = ""
        for i in range(1, n + 1):
            s += str(i)
        return int(s[n - 1])
            
            
    
s = Solution()
print(s.findNthDigit(3))
print(s.findNthDigit(11))
print(s.findNthDigit(2147983))