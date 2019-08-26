# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
pick = 2
def guess(num):
    if num < pick:
        return 1
    elif num > pick:
        return -1
    else:
        return 0

class Solution(object):
    
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 1
        e = n
        while s <= e:
            c = (e - s) // 2 + s
            j = guess(c)
            if j > 0:
                s = c + 1
            elif j < 0:
                e = c - 1
            else:
                return c
        return n
    
    
s = Solution()
print(s.guessNumber(2))
