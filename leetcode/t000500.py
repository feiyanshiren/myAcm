from typing import List

class Solution:
    def __init__(self):
        self.s1 = set("qwertyuiop")
        self.s2 = set("asdfghjkl")
        self.s3 = set("zxcvbnm")
    
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        for i in words:
            a = set(i.lower())
            if a & self.s1 == a:
                res.append(i)
            elif a & self.s2 == a:
                res.append(i)
            elif a & self.s3 == a:
                res.append(i)
        return res 

s = Solution()
print(s.findWords(["Hello", "Alaska", "Dad", "Peace"]))

