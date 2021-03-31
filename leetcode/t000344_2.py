class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        if l > 2:
            i = 0
            j = l - 1
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

s = Solution()
a = ["h","e","l","l","o"]
b = ["H","a","n","n","a","h"]
c = []
d = ["h","e","l","l","o"]
s.reverseString(a)
s.reverseString(b)
s.reverseString(c)
s.reverseString(d)


print(a)
print(b)
print(c)
print(d)

