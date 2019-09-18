
from typing import List
import collections
import time

t = time.time() 
"""
滑动窗口思想，保留了每一次之前没有改变的值，少算了很多
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        left = 0
        right = 0
        needs = {}
        window = {}
        for i in p:
            needs[i] = needs.get(i, 0) + 1
        match = 0
        
        l1 = len(s)
        l2 = len(p)
        while right < l1:
            c1 = s[right]
            if c1 in needs:
                window[c1] = window.get(c1, 0) + 1
                if window[c1] == needs[c1]:
                    match += 1
            right += 1
            
            while match == len(needs):
                if right - left == l2:
                    res.append(left)
                c2 = s[left]
                if c2 in needs:
                    window[c2] = window.get(c2, 0) - 1
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1
        return res
                
        
 
s = Solution()
print(s.findAnagrams("cbaebabacd", "abc"))
print(s.findAnagrams("abab", "ab"))


print(time.time() - t)