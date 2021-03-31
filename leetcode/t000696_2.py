class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        old = 0
        count = 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                res += min(old, count)
                old = count
                count = 1
            else:
                count += 1
        return res + min(old, count)
        
"""
我们可以修改我们的方法 1 来实时计算答案。我们将只记住 prev = groups[-2] 和 cur=groups[-1] 来代替 groups。然后，答案是我们看到的每个不同的 (prev, cur) 的 min(prev, cur) 之和。

"""           

s = Solution()
print(s.countBinarySubstrings("00110011"))
print(s.countBinarySubstrings("10101"))