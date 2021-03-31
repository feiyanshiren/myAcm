class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        k2 = 2 * k
        c = len(s) // k2 + 1
        a = []
        for i in range(c):
            a.append(s[i * k2: i * k2 + k2])
        res = ""
        for i in a:
            if len(i) <= k:
                res += i[::-1]
            else:
                res += i[:k][::-1] + i[k:]
        return res
    
s = Solution()
print(s.reverseStr("abcdefg", 2))