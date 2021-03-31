class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(' ')
        L = s.split(' ')[-1]
        return len(L)
        


s = Solution()
print(s.lengthOfLastWord("a "))