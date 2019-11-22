class Solution:
    def reverseWords(self, s: str) -> str:
        s1 = ""
        s2 = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                s2 += s[i]
            else:
                s1 = s2 + " " + s1
                s2 = ""
        if s2 != "":
            s1 = s2 + " " + s1
        return s1.strip()
    
s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
import time

t1 = time.time()
for i in range(100000):
    s.reverseWords("Let's take LeetCode contest")
print(time.time() - t1)
