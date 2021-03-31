class Solution:
    def convertToBase7(self, num: int) -> str:
        a = ""
        if num < 0:
            num = -num
            a = "-"
        b = ""
        while 1:
            s = num // 7
            y = num % 7
            b = str(y) + b
            if s == 0:
                break
            num = s
        return a + b
    
s = Solution()
print(s.convertToBase7(100))
print(s.convertToBase7(-7))


# a = int("202", base=7)
# print(a)