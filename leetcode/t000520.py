class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.islower():
            return True
        else:
            word = word[1:]
            if word.islower():
                return True
            elif word.isupper():
                return True
            else:
                return False
            

s = Solution()
print(s.detectCapitalUse("USA"))
print(s.detectCapitalUse("FlaG"))