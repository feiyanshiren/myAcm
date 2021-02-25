from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        aa = {}
        bb = {}
        res = []
        for i in A.split():
            aa[i] = aa.get(i, 0) + 1
        for i in B.split():
            bb[i] = bb.get(i, 0) + 1
        for k, v in aa.items():
            if v == 1:
                if k not in bb:
                    res.append(k)
        for k, v in bb.items():
            if v == 1:
                if k not in aa:
                    res.append(k)
        return res


# ```
# ---
#
# 884.
# 两句话中的不常见单词 - -2
#
# 给定两个句子
# A
# 和
# B 。 （句子是一串由空格分隔的单词。每个单词仅由小写字母组成。）
#
# 如果一个单词在其中一个句子中只出现一次，在另一个句子中却没有出现，那么这个单词就是不常见的。
#
# 返回所有不常用单词的列表。
#
# 您可以按任何顺序返回列表。
#
#
#
# 示例
# 1：
#
# 输入：A = "this apple is sweet", B = "this apple is sour"
# 输出：["sweet", "sour"]
#
# 示例
# 2：
#
# 输入：A = "apple apple", B = "banana"
# 输出：["banana"]
#
# 提示：
#
# 0 <= A.length <= 200
# 0 <= B.length <= 200
# A
# 和
# B
# 都只包含空格和小写字母。
#
# 解：
# 根据解法一优化成使用一个字典。
#
#
# ```py


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        C = A.split(' ') + B.split(' ')
        return [i for i in C if C.count(i) == 1]


