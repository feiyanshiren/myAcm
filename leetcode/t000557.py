class Solution:
    def reverseWords(self, s: str) -> str:
        s1 = s.split(" ")
        s2 = ""
        for i in s1:
            s2 += i[::-1] + " "
        return s2.strip()
    
s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
import time

t1 = time.time()
for i in range(100000):
    s.reverseWords("Let's take LeetCode contest")
print(time.time() - t1)
