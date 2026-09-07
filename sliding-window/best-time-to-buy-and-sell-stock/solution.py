class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        minprice = prices[0]
        for price in prices:
            if(minprice> price):
                minprice = price
            else:
                profit = max(profit,price-minprice)
        return profit
