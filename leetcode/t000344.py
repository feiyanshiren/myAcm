class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        a = []
        while len(s):
            a.append(s.pop(0))
        while len(a):
            s.append(a.pop())
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

