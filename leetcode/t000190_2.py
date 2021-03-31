class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(bin(n)[2:].zfill(32)[::-1],2)
    
s = Solution()
print(s.reverseBits(43261596))
print(s.reverseBits(4294967293))