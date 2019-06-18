class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        a = str(bin(n))[2:]
        while len(a) < 32:
            a = "0" + a
        return int(a[::-1], base=2)
    
s = Solution()
print(s.reverseBits(43261596))
print(s.reverseBits(4294967293))