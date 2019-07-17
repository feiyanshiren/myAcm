# 比较巧妙，对比两个字符串对应位置的字符在字符串内第一次出现的位置。

class Solution:
    def isIsomorphic(self, s, t):
        for i in range(len(s)):
            if s.find(s[i]) != t.find(t[i]):
                return False
        return True
                
                
     
s = Solution()
print(s.isIsomorphic("egg", "add"))   
print(s.isIsomorphic("foo", "bar"))   
print(s.isIsomorphic("paper", "title"))   