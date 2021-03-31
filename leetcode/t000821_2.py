# 821. 字符的最短距离    --2
#
# 给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。
#
# 示例 1:
#
# 输入: S = "loveleetcode", C = 'e'
# 输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
#
# 说明:
#
#     字符串 S 的长度范围为 [1, 10000]。
#     C 是一个单字符，且保证是字符串 S 里的字符。
#     S 和 C 中的所有字母均为小写字母。
#
# 解：
# 左遍历一次加右遍历一次就可以了。
#
# ```
from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        l = len(S)
        res1 = [l for i in range(l)]
        res2 = [l for i in range(l)]

        d = 0
        for i in range(l):
            if S[i] == C:
                for j in range(d, i + 1):
                    res1[j] = i - j
                d = i + 1
        d = l - 1
        for i in range(l - 1, -1, -1):
            if S[i] == C:
                for j in range(d, i - 1, -1):
                    res2[j] = j - i
                d = i - 1
        res = []
        for i in range(l):
            res.append(min(res1[i], res2[i]))
        return res