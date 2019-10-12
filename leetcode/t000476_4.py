class Solution:
    def findComplement(self, num: int) -> int:
        t = num
        c = 0
        while t > 0:
            t >>= 1
            c = (c << 1) + 1
        return num ^ c
        
s = Solution()
print(s.findComplement(5))
print(s.findComplement(1))
print(s.findComplement(0))
print(s.findComplement(-1))