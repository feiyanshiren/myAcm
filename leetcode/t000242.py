class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        a = {}
        b = {}
        for i in s:
            a[i] = a.get(i, 0) + 1
        for i in t:
            b[i] = b.get(i, 0) + 1
        res = True
        for k, v in a.items():
            if v != b.get(k, 0):
                res = False
                break
        return res
   
s = Solution()
print(s.isAnagram("123", "1232"))
print(s.isAnagram("1223", "1232"))