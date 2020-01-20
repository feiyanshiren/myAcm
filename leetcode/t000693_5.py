class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n == 1:
            return True
        temp = bin(n)[2:]
        return len(set(temp[::2])) == 1 and len(set(temp[1::2])) == 1 and set(temp[::2]) != set(temp[1::2])




"""
把数组分割为奇数索引数组和偶数索引数组判断。
"""
s = Solution()
print(s.hasAlternatingBits(5))
print(s.hasAlternatingBits(7))
print(s.hasAlternatingBits(11))
print(s.hasAlternatingBits(10))
print(s.hasAlternatingBits(9223372036854775807))