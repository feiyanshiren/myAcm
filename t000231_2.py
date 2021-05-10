class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return bin(n).count("1") == 1
       
   
s = Solution()
print(s.isPowerOfTwo(1)) 
print(s.isPowerOfTwo(16)) 
print(s.isPowerOfTwo(218)) 
print(s.isPowerOfTwo(123)) 
print(s.isPowerOfTwo(100)) 
print(s.isPowerOfTwo(234))
print(s.isPowerOfTwo(0))