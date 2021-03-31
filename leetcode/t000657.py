class Solution:
    def judgeCircle(self, moves: str) -> bool:
        s = 0
        c = 0
        for i in moves:
            if i == "L":
                s += -1
            elif i == "R":
                s += 1
            elif i == "U":
                c += 1
            elif i == "D":
                c += -1
        if s == 0 and c == 0:
            return True
        else:
            return False


s = Solution()
print(s.judgeCircle("UD"))
print(s.judgeCircle("LL"))