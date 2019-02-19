class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices) == 0:
            return 0
        t_prices = prices.copy()
        t_prices.sort()
        k = 0
        for i in t_prices:
            imi = prices.index(i)
            if imi != len(prices) - 1:
                t_list = prices[imi + 1:]
                mx = max(t_list)
                a = mx - i
                if k <= a:
                    k = a
        return k

s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([7, 6, 4, 3, 1]))
print(s.maxProfit([]))
print(s.maxProfit(None))
print(s.maxProfit([2, 4, 1]))
