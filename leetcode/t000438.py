
from typing import List
import collections
import time

t = time.time() 

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l1 = len(s)
        l2 = len(p)
        if l1 < l2:
            return []
        res = []
        c = collections.Counter(p)
        for i in range(l1 - l2 + 1):
            if c == collections.Counter(s[i: i + l2]):
                res.append(i)
        return res 
                
        
 
s = Solution()
print(s.findAnagrams("cbaebabacd", "abc"))
print(s.findAnagrams("abab", "ab"))


print(time.time() - t)