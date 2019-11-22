class Solution:
    def reverseWords(self, s: str) -> str:
        a = []
        s1 = ""
        for i in s:
            if i != " ":
                a.append(i)
            else:
                while len(a) != 0:
                    s1 += a.pop()
                s1 += " "
        return s1.strip()
    
s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
import time

t1 = time.time()
for i in range(100000):
    s.reverseWords("Let's take LeetCode contest")
print(time.time() - t1)
