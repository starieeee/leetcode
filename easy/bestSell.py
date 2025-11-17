class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # minValue = min(prices)
        # maxValue = max(prices)

        # minIndex = prices.index(minValue)
        # maxIndex = prices.index(maxValue)

        # if maxIndex < minIndex:
        #     return 0
        # else:
        #     return maxValue - minValue
        minPrice = float('inf')
        maxp = 0
        for price in prices:
            minPrice = min(minPrice, price)
            profit = price - minPrice
            maxp = max(maxp, profit)
        return maxp