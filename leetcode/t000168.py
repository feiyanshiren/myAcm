class Solution:
    def convertToTitle(self, n: int) -> str:
        j = ""
        while n > 26:
            m = n % 26
            n = n // 26
            if m == 0:
                j = "Z" + j
                n -= 1
            else:
                j = chr(m + 64) + j
        if n != 0:
            j = chr(n + 64) + j
        return j
           
           
       
s = Solution()
print(s.convertToTitle(1))
print(s.convertToTitle(2))
print(s.convertToTitle(3))
print(s.convertToTitle(26))
print(s.convertToTitle(27))
print(s.convertToTitle(28))
print(s.convertToTitle(701))
print(s.convertToTitle(702))
print(s.convertToTitle(703))
