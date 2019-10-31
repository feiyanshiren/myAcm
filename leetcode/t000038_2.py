class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        else:
            import re
            str1=""
            pattern=re.compile(r'(\d)\1{0,}')
            for i in pattern.finditer(self.countAndSay(n-1)):
                str1 += str(len(i.group(0))) + i.group(0)[0]
            return str1