class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if prices == []:
            return 0
        
        minPrice = prices[0] 
        maxProfit = 0

        for i in range(1, len(prices)): 
            if prices[i] < minPrice: 
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProfit: 
                maxProfit = prices[i] - minPrice        
        return maxProfit

