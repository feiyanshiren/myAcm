class Solution:
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        r = 0
        while x > r:
            r = r * 10 + x % 10
            x //= 10
        return x == r or x == r // 10
        

s = Solution()
print(s.isPalindrome(-120))
print(s.isPalindrome(121))
print(s.isPalindrome(120))
print(s.isPalindrome(1221))


