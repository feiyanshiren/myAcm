# 821. 字符的最短距离
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
# 暴力遍历,对于每个字符左右遍历再比较
#
# ```
from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        res = []
        l = len(S)
        for i in range(l):
            if S[i] == C:
                res.append(0)
            else:
                m1 = 0
                m2 = 0
                a = 0
                for j in range(i, 0, -1):
                    if S[j] == C:
                        a = 1
                        break
                    m1 += 1
                if a == 0:
                    m1 = 0
                a = 0
                for j in range(i, l):
                    if S[j] == C:
                        a = 1
                        break
                    m2 += 1
                if a == 0:
                    m2 = 0
                if m1 != 0 and m2 != 0:
                    res.append(min(m1, m2))
                else:
                    k = m1 if m1 != 0 else m2
                    res.append(k)
        return res