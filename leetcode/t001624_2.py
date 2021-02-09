class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        len_s = len(s)
        max_s = -1
        for i in range(len_s):
            j = s.rfind(s[i])
            if j != -1 and j != i:
                max_s = max(max_s, j - i - 1)
        return max_s


s = Solution()
print(s.maxLengthBetweenEqualCharacters("aa"))
print(s.maxLengthBetweenEqualCharacters("abca"))
print(s.maxLengthBetweenEqualCharacters("cbzxy"))
print(s.maxLengthBetweenEqualCharacters("cabbac"))
print(s.maxLengthBetweenEqualCharacters("mgntdygtxrvxjnwksqhxuxtrv"))
