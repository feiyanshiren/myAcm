class Solution:
    def __init__(self):
        self.m_y = set(["a", "e", "i", "o", "u",
                       "A", "E", "I", "O", "U"])
        
    def reverseVowels(self, s: str) -> str:
        l, h = 0, len(s) - 1
        s_s = list(s)
        while l < h:
            if s_s[h] not in self.m_y:
                h -= 1
            if s_s[l] not in self.m_y:
                l += 1
            if s_s[l] in self.m_y and s_s[h] in self.m_y:
                s_s[l], s_s[h] = s_s[h], s_s[l]
                l += 1
                h -= 1
        return "".join(s_s)


s = Solution()
print(s.reverseVowels("hello"))
print(s.reverseVowels("leetcode"))
print(s.reverseVowels(""))
print(s.reverseVowels("e"))
print(s.reverseVowels("l"))