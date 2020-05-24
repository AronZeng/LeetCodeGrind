class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2: 
            return 0
        peak = prices[0]
        valley = prices[0]
        max = 0
        for i in range(1,len(prices)): 
            if prices[i] < valley: 
                valley = prices[i]
                peak = 0
            elif prices[i] > peak: 
                peak = prices[i]
            if peak - valley > max:
                max = peak - valley
        return max