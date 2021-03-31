class Solution:
    def toDo(self, n, l):
        if n == 1:
            return True
        else:
            s = str(n)
            w = 0
            for i in s:
                w += int(i) ** 2
            if w in l:
                return False
            else:
                l.append(w)
                return self.toDo(w, l)
    
    def isHappy(self, n):
        return self.toDo(n, [])
        

s = Solution()
# print(s.isHappy(19))
print(s.isHappy(20))
