from typing import List

class Solution:
    def __init__(self):
        self.s1 = "qwertyuiop"
        self.s2 = "asdfghjkl"
        self.s3 = "zxcvbnm"
    
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        for i in words:
            a = i.lower()
            if a.strip(self.s1) == "":
                res.append(i)
            elif a.strip(self.s2) == "":
                res.append(i)
            elif a.strip(self.s3) == "":
                res.append(i)
        return res 

s = Solution()
print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))

