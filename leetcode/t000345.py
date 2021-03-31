class Solution:
    def __init__(self):
        self.m_y = set(["a", "e", "i", "o", "u",
                       "A", "E", "I", "O", "U"])
        
    def reverseVowels(self, s: str) -> str:
        f_i = []
        for i in s:
            if i in self.m_y:
                f_i.append(i)
        s_s = list(s)
        for i in range(len(s_s)):
            k = s_s[i]
            if k in self.m_y:
                s_s[i] = f_i.pop()
        return "".join(s_s)


s = Solution()
print(s.reverseVowels("hello"))
print(s.reverseVowels("leetcode"))
print(s.reverseVowels(""))
print(s.reverseVowels("e"))
print(s.reverseVowels("l"))