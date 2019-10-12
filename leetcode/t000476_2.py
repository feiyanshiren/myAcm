class Solution:
    def findComplement(self, num: int) -> int:
        return int(bin(num)[2:].replace("0", "x").replace("1", "0").replace("x", "1"), 2)
        
s = Solution()
print(s.findComplement(5))
print(s.findComplement(1))
print(s.findComplement(0))
# print(s.findComplement(-1))