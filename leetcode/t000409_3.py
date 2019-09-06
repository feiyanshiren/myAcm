class Solution(object):
    def longestPalindrome(self, s: str) -> int:
        counter = {c: s.count(c) for c in set(s)}    # 字符计数集
        return sum(count >> 1 << 1 for count in counter.values()) + \
               (1 if any(count & 1 for count in counter.values()) else 0)

