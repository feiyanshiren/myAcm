class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        z = []
        for s_i in s:
            if s_i == "(" or s_i == "[" or s_i == "{":
                z.append(s_i)
            elif s_i == ")":
                if len(z) != 0 and "(" == z[-1]:
                    z.pop()
                else:
                    z.append(s_i)
            elif s_i == "]":
                if len(z) != 0 and "[" == z[-1]:
                    z.pop()
                else:
                    z.append(s_i)
            else:
                if len(z) != 0 and "{" == z[-1]:
                    z.pop()
                else:
                    z.append(s_i)
        if len(z) == 0:
            return True
        else:
            return False
            
s = Solution()
print(s.isValid("(([]){})"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([)]"))
print(s.isValid("{[]}"))