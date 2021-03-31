# 解：
# 用栈模拟
#
# ```


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        a = []
        for i in S:
            if i == "#":
                if len(a):
                    a.pop()
            else:
                a.append(i)
        b = []
        for i in T:
            if i == "#":
                if len(b):
                    b.pop()
            else:
                b.append(i)
        if a == b:
            return True
        else:
            return False


# 解：
# 用栈模拟，再精简优化
#
# ```


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        if self.typed(S) == self.typed(T):
            return True
        else:
            return False

    def typed(self, s):
        a = []
        for i in s:
            if i == "#" and a:
                a.pop()
            else:
                a.append(i)
        return a


# 844.
# 比较含退格的字符串 - -3
#
# 给定
# S
# 和
# T
# 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。  # 代表退格字符。
#
#
# 示例
# 1：
#
# 输入：S = "ab#c", T = "ad#c"
# 输出：true
# 解释：S
# 和
# T
# 都会变成 “ac”。
#
# 示例
# 2：
#
# 输入：S = "ab##", T = "c#d#"
# 输出：true
# 解释：S
# 和
# T
# 都会变成 “”。
#
# 示例
# 3：
#
# 输入：S = "a##c", T = "#a#c"
# 输出：true
# 解释：S
# 和
# T
# 都会变成 “c”。
#
# 示例
# 4：
#
# 输入：S = "a#c", T = "b"
# 输出：false
# 解释：S
# 会变成 “c”，但
# T
# 仍然是 “b”。
#
#
#
# 提示：
#
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S
# 和
# T
# 只含有小写字母以及字符
# '#'。

# 解：
# 其实倒序排查就好
#
# ```


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        if self.typed(S) == self.typed(T):
            return True
        else:
            return False

    def typed(self, s):
        a = ""
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "#":
                count += 1
            else:
                if count:
                    count -= 1
                    continue
                else:
                    a = s[i] + a
        return a
