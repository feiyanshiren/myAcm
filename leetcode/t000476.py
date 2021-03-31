class Solution:
    def findComplement(self, num: int) -> int:
        b1 = bin(num)
        l1 = len(b1) - 2
        s1 = ""
        for i in range(l1):
            s1 += "1"
        n1 = int(s1, 2)
        return ~num & n1
        
s = Solution()
print(s.findComplement(5))
print(s.findComplement(1))
print(s.findComplement(0))
print(s.findComplement(-1))