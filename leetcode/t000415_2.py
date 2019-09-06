class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = {str(i):i for i in range(10)}
        s1 = 0
        s2 = 0
        l1 = len(num1)
        l2 = len(num2)
        for i in range(l1):
            s1 += m[num1[i]] * (10 ** (l1 - i - 1))
        for i in range(l2):
            s2 += m[num2[i]] * (10 ** (l2 - i - 1))
        return str(s1 + s2)
    
s = Solution()
print(s.addStrings("123", "456"))