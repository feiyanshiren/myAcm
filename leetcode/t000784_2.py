# 784. 字母大小写全排列    --2
#
# 给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。
#
# 示例:
# 输入: S = "a1b2"
# 输出: ["a1b2", "a1B2", "A1b2", "A1B2"]
#
# 输入: S = "3z4"
# 输出: ["3z4", "3Z4"]
#
# 输入: S = "12345"
# 输出: ["12345"]
#
# 注意：
#
#     S 的长度不超过12。
#     S 仅由数字和字母组成。
#
# 解：
# 递归【通过】
#
# 思路
#
# 从左往右依次遍历字符，过程中保持 ans 为已遍历过字符的字母大小全排列。
#
# 例如，当 S = "abc" 时，考虑字母 "a", "b", "c"，初始令 ans = [""]，依次更新 ans = ["a", "A"]， ans = ["ab", "Ab", "aB", "AB"]， ans = ["abc", "Abc", "aBc", "ABc", "abC", "AbC", "aBC", "ABC"]。
#
# 算法
#
# 如果下一个字符 c 是字母，将当前已遍历过的字符串全排列复制两份，在第一份的每个字符串末尾添加 lowercase(c)，在第二份的每个字符串末尾添加 uppercase(c)。
#
# 如果下一个字符 c 是数字，将 c 直接添加到每个字符串的末尾。
#
# ```
class Solution(object):
    def letterCasePermutation(self, S):
        ans = [[]]

        for char in S:
            n = len(ans)
            if char.isalpha():
                for i in range(n):
                    ans.append(ans[i][:])
                    ans[i].append(char.lower())
                    ans[n+i].append(char.upper())
            else:
                for i in range(n):
                    ans[i].append(char)

        return map("".join, ans)