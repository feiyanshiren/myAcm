class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        len_s = len(s)
        max_s = -1
        for i in range(len_s):
            for j in range(len_s - 1, i, -1):
                if s[i] == s[j]:
                    max_s = max(max_s, j - i - 1)
                    break
        return max_s


s = Solution()
print(s.maxLengthBetweenEqualCharacters("aa"))
print(s.maxLengthBetweenEqualCharacters("abca"))
print(s.maxLengthBetweenEqualCharacters("cbzxy"))
print(s.maxLengthBetweenEqualCharacters("cabbac"))
print(s.maxLengthBetweenEqualCharacters("mgntdygtxrvxjnwksqhxuxtrv"))
