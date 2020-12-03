# 720. 词典中最长的单词    --2
# 题目描述
#
#
# 给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。
#
# 若无答案，则返回空字符串。
#
# 示例 1:
#
# 输入:
# words = ["w","wo","wor","worl", "world"]
# 输出: "world"
# 解释:
# 单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。
#
# 示例 2:
#
# 输入:
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# 输出: "apple"
# 解释:
# "apply"和"apple"都能由词典中的单词组成。但是"apple"得字典序小于"apply"。
#
# 注意:
#
#     所有输入的字符串都只包含小写字母。
#     words数组长度范围为[1,1000]。
#     words[i]的长度范围为[1,30]。
#
# 解：
# 暴力法
#
# 对于每个单词，我们可以检查它的全部前缀是否存在，可以通过 Set 数据结构来加快查找
#
# 算法：
#
#     当我们找到一个单词它的长度更长且它的全部前缀都存在，我们将更改答案。
#     或者，我们可以事先将单词排序，这样当我们找到一个符合条件的单词就可以认定它是答案。
#
# ```
class Solution(object):
    def longestWord(self, words):
        ans = ""
        wordset = set(words)
        for word in words:
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                if all(word[:k] in wordset for k in xrange(1, len(word))):
                    ans = word

        return ans