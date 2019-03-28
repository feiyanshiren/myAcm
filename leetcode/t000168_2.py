class Solution:
    def convertToTitle(self, n: int) -> str:
        # 递归处理
        if (n-1)//26 == 0:
            return chr( 65 + (n-1) % 26 )
        else:
            return self.convertToTitle( (n-1)//26 ) + chr(65 + (n-1) % 26)

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
