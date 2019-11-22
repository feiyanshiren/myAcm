class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s[::-1].split(" ")[::-1])
 
s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
import time

t1 = time.time()
for i in range(100000):
    s.reverseWords("Let's take LeetCode contest")
print(time.time() - t1)
