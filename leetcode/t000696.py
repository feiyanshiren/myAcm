class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 1
        old = s[0]
        lens = len(s)
        g = []
        for i in range(1, lens):
            if old == s[i]:
                count += 1
            else:
                g.append(count)
                count = 1
                old = s[i]
        g.append(count)
        
                
        res = 0
        for i in range(1, len(g)):
            res += min(g[i - 1], g[i])
        return res
            
"""
我们可以将字符串 s 转换为 groups 数组表示字符串中相同字符连续块的长度。例如，如果 s=“11000111000000”，则 groups=[2，3，4，6]。

对于 '0' * k + '1' * k 或 '1' * k + '0' * k 形式的每个二进制字符串，此字符串的中间部分必须出现在两个组之间。

让我们尝试计算 groups[i] 和 groups[i+1] 之间的有效二进制字符串数。如果我们有 groups[i] = 2, groups[i+1] = 3，那么它表示 “00111” 或 “11000”。显然，我们可以在此字符串中生成 min(groups[i], groups[i+1]) 有效的二进制字符串。

"""

s = Solution()
print(s.countBinarySubstrings("00110011"))
print(s.countBinarySubstrings("10101"))