class Solution:
    def findComplement(self, num: int) -> int:
        i = 1
        t = num
        while t != 1:
            t //= 2
            i += 1
        a = 2 ** i - 1
        return num ^ a
        
s = Solution()
print(s.findComplement(5))
print(s.findComplement(1))
print(s.findComplement(0))
# print(s.findComplement(-1))