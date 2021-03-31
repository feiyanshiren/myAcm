class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxP = 0
        for i in range(len(prices) - 1):
            dif = prices[i+1] - prices[i]
            if dif > 0:
                maxP += dif
        return maxP
