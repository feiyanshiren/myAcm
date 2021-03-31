class Solution:
    def findComplement(self, num: int) -> int:
        l = len(bin(num)[2:])
        n = 2 ** l -1
        return num ^ n
        
s = Solution()
print(s.findComplement(5))
print(s.findComplement(1))
print(s.findComplement(0))
print(s.findComplement(-1))