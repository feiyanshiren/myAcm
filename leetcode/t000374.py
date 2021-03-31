# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
pick = 6
def guess(num):
    if num < pick:
        return 1
    elif num > pick:
        return -1
    else:
        return 0

class Solution(object):
    def dd(self, s, e):
        if s > e:
            return s
        d = e - s
        b = d // 2 + s
        c = guess(b)
        if c == 1:
            s = b + 1
            return self.dd(s, e)
        elif c == -1:
            e = b - 1
            return self.dd(s, e)
        else:
            return b
    
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.dd(1, n)
    
    
s = Solution()
print(s.guessNumber(10))
