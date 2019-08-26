class Solution(object):
    def findTheDifference(self, s: str, t: str) -> str:
        a = 0
        for i in s:
            a ^= ord(i)
        for i in t:
            a ^= ord(i)
        return chr(a)

    
s = Solution()
print(s.findTheDifference("abcd", "abcde"))
print(s.findTheDifference("a", "b"))