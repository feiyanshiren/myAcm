class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
            

s = Solution()
print(s.detectCapitalUse("USA"))
print(s.detectCapitalUse("FlaG"))