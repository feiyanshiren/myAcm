class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')


s = Solution()
print(s.judgeCircle("UD"))
print(s.judgeCircle("LL"))