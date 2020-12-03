# 720. 词典中最长的单词    --3
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
# 前缀树 + 深度优先搜索
#
# 由于涉及到字符串的前缀，通常可以使用 trie（前缀树）来解决。
#
# 算法：
#
#     将所有单词插入 trie，然后从 trie 进行深度优先搜索，每找到一个单词表示该单词的全部前缀均存在，我们选取长度最长的单词。
#     在 python 中，我们使用了 defaultdict 的方法。而在 java 中，我们使用了更通用的面向对象方法。
#
#
#
# ```
import collections
from functools import reduce


class Solution(object):
    def longestWord(self, words):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i

        stack = trie.values()
        ans = ""
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])

        return ans