class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        m = {i: "" for i in pattern}
        s = str.split()
        n = {i: "" for i in s}
        if len(m.keys()) != len(n.keys()):
            return False
        l1 = list(m.keys())
        l2 = list(n.keys())
        f = {}
        for i in range(len(l1)):
            f[l1[i]] = l2[i]
        str1 = ""
        for i in pattern:
            str1 += f.get(i, "")
            str1 += " "
        if str1 == str + " ":
            return True
        else:
            return False
            
    

s = Solution()
print(s.wordPattern("abba", "dog cat cat dog"))
print(s.wordPattern("abba", "dog cat cat fish"))
print(s.wordPattern("aaaa", "dog cat cat dog"))
print(s.wordPattern("abba", "dog dog dog dog"))
print(s.wordPattern("", ""))
print(s.wordPattern("abc", "b c a"))