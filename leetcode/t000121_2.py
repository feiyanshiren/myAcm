class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        动态规划 前i天的最大收益 = max{前i-1天的最大收益，第i天的价格-前i-1天中的最小价格}
        """
        min_p, max_p = 999999, 0
        for i in range(len(prices)):
            min_p = min(min_p, prices[i])
            max_p = max(max_p, prices[i] - min_p)
        return max_p

s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([7, 6, 4, 3, 1]))
print(s.maxProfit([]))
print(s.maxProfit(None))
print(s.maxProfit([2, 4, 1]))
