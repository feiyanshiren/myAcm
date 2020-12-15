# 784. 字母大小写全排列
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
# 先分解,在使用库函数组合,在踢出多余的
#
# ```
import itertools

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if not S:
            return []
        elif S == "":
            return []
        elif S.isdigit():
            return [S]
        else:
            a = []
            b = ""
            for i in range(len(S)):
                b += S[i]
                if S[i].isalpha():
                    a.append(b)
                    b = ""
            if b != "":
                a[len(a) - 1] += b
            # print(a)
            d = []
            for i in a:
                d.append(i.lower())
                d.append(i.upper())
            e = "".join(a)
            e = e.lower()
            f = ["".join(i) for i in itertools.combinations(d, len(a))]
            g = []
            for i in f:
                if e == i.lower() and i not in g:
                    g.append(i)
            return g