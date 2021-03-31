from collections import Counter


class Solution(object):

    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)    # 字符计数集

        # 累加每个字符个数的最大偶数，最终结果为回文串最大长度
        palindrome_length = sum(count >> 1 << 1 for count in counter.values())

        # 是否存在任意字符个数为奇数个；如果存在，则需要增一到回文串最大长度上
        add_odd = 1 if any(count & 1 for count in counter.values()) else 0

        # 返回回文串最大长度
        return palindrome_length + add_odd

