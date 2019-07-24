class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
       if n <= 0:
           return False
       elif n == 1:
           return True
       else:
           if n % 2 == 0:
               return self.isPowerOfTwo(n // 2)
           else:
               return False
       
   
s = Solution()
print(s.isPowerOfTwo(1)) 
print(s.isPowerOfTwo(16)) 
print(s.isPowerOfTwo(218)) 
print(s.isPowerOfTwo(123)) 
print(s.isPowerOfTwo(100)) 
print(s.isPowerOfTwo(234))
print(s.isPowerOfTwo(0))