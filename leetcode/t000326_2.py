class Solution:
            
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n //= 3
        
        return n == 1
    

s = Solution()
print(s.isPowerOfThree(27))
print(s.isPowerOfThree(0))
print(s.isPowerOfThree(9))
print(s.isPowerOfThree(45))
print(s.isPowerOfThree(1))

# 基准转换 转3进制 形式为10000
# 运算法 return (Math.log10(n) / Math.log10(3)) % 1 == 0;
# 整数限制 return n > 0 && 1162261467 % n == 0;