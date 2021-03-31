class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.islower():
            return True
        else:
            word = word[1:]
            return word.isupper() or word.islower()
            

s = Solution()
print(s.detectCapitalUse("USA"))
print(s.detectCapitalUse("FlaG"))