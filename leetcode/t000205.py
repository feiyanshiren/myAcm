class Solution:
    def isIsomorphic(self, s, t):
        m1, m2 = list({k: 0 for k in s}.keys()), list({k: 0 for k in t}.keys())
        l1, l2 = len(m1), len(m2)
        if l1 != l2:
            return False
        else:
            m = {}
            for i in range(l1):
                m[m1[i]] = m2[i]
            k = ""
            for i in s:
                k += m.get(i, "")
            if k == t:
                return True
            else:
                return False
                
                
     
s = Solution()
print(s.isIsomorphic("egg", "add"))   
print(s.isIsomorphic("foo", "bar"))   
print(s.isIsomorphic("paper", "title"))   