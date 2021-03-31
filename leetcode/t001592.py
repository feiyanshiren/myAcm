class Solution:
    def reorderSpaces(self, text: str) -> str:
        k = text.count(" ")
        s = [i for i in text.split(" ") if i != ""]
        cs = len(s)
        if cs == 0:
            return text
        if cs > 1:
            d = k % (cs - 1)
            e = k // (cs - 1)
            res = []
            for i in s:
                res.append(i)
                res.append(" " * e)
            res.pop()
            res.append(" " * d)
            return "".join(res)
        elif cs == 1:
            if k != 0:
                d = " " * k
                return s[0] + d
            else:
                return s[0]

s = Solution()
print(s.reorderSpaces("  this   is  a sentence "))